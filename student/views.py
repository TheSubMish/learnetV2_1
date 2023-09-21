from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import json

from .forms import UserInformationForm,UserPreferenceForm
from .models import Student,UserPreference
from userlog.models import CustomUser
from .get_or_create import get_user_information,get_user_preferences,user_info_function,save_user_name,update_user_information,create_pref,update_pref

# Create your views here.
class StudentDashboard(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    template_name = 'studash.html'
    success_url = reverse_lazy('student_dashboard')
    userform = UserInformationForm
    prefForm = UserPreferenceForm

    def get(self,request,error=None):
        username = request.user.username
        try:
            currentuser = CustomUser.objects.get(username=username)
            currentuserinfo = Student.objects.get(user=currentuser)
        except Student.DoesNotExist:
            return redirect(self.login_url)

        # get current user informations from database main code is in get_or_create.py    
        self.userform = get_user_information(currentuser,currentuserinfo)
        # get current user preferences from database main code is in get_or_create.py
        userPref = get_user_preferences(request)
        if userPref is None:
            return render(request,self.template_name,{'userform':self.userform,'prefform': self.prefForm,'pic':currentuserinfo,'error':error})
        else:
            self.prefForm = userPref
            return render(request,self.template_name,{'userform':self.userform,'prefform': self.prefForm,'pic':currentuserinfo,'error':error})
        
    def post(self,request,error=None):
        user_info_form_data = self.userform(request.POST,request.FILES)
        if user_info_form_data.is_valid():
            save_user_name(user_info_form_data.cleaned_data,request.user.username)
            if user:=Student.objects.get(user=request.user):
                update_user_information(user_info_form_data.cleaned_data,user)
            else:
                user_info_form_data.save()
        else:
            error_msg_dict = json.loads(user_info_form_data.errors.as_json())
            if error_msg_dict['phone']:
                error_msg = error_msg_dict['phone'][0]['message']
            else:
                error_msg = error_msg_dict['__all__'][0]['message']
            return redirect('student_dashboard_error',error_msg)
        
        user_preferences_data = self.prefForm(request.POST)
        if user_preferences_data.is_valid():
            user = Student.objects.get(user=request.user)
            try:
                prefUser=UserPreference.objects.get(user=user)
                update_pref(user_preferences_data.cleaned_data,prefUser)
            except UserPreference.DoesNotExist:
                create_pref(user_preferences_data.cleaned_data,user)
            return redirect(self.success_url)
        