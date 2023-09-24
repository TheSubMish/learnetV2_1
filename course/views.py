from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.text import slugify
import json

from .models import Course,Chapter,Test
from .forms import CourseForm,ChapterForm,TestForm
from .validations import course_validate,chapter_validate,test_vlaidate
from .create_get import create_test
from teacher.models import Teacher 

# Create your views here.
class AddCourse(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    template_name = 'addCourse.html'
    model = Course
    form_class = CourseForm

    def get(self,request):
        try:
            Teacher.objects.get(user=request.user)
            return render(request,self.template_name,{'form':self.form_class})
        except Teacher.DoesNotExist:
            return redirect(self.login_url)

    def post(self,request):
        course_data = self.form_class(request.POST,request.FILES)
        if course_data.is_valid():
            if error_msg:= course_validate(course_data.cleaned_data):
                return render(request,self.template_name,{'form':course_data,'error':error_msg})
            else:
                teacher = Teacher.objects.get(user=request.user)
                Course.objects.create(teacher=teacher,**course_data.cleaned_data,slug=slugify(course_data.cleaned_data['courseTitle']))
                url = reverse('addchapter', kwargs={'course_slug': slugify(course_data.cleaned_data['courseTitle'])})
                return redirect(url)
        else:
            error_msg = json.loads(course_data.errors.as_json())
            print(error_msg)
            try:
                if error_msg['category']:
                    error_msg['category'] = "Select Category Of Your Course"
                    return render(request,self.template_name,{'form':course_data,'error':error_msg})
            except KeyError:
                pass

            if error_msg['courseTitle']:
                error_msg['courseTitle'] = "Course With This Name Already Exists"
                return render(request,self.template_name,{'form':course_data,'error':error_msg})
            
class AddChapter(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    template_name = 'addChapter.html'
    model = Chapter
    form_class = ChapterForm

    def get(self,request,course_slug=None):
        try:
            Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            return redirect(self.login_url)

        course = Course.objects.get(slug=course_slug)
        self.form_class = self.form_class(initial={'course':course})
        return render(request,self.template_name,{'form':self.form_class})
    
    def post(self,request,course_slug=None):
        chapter_data = self.form_class(request.POST)
        if chapter_data.is_valid():
            if error_msg:=chapter_validate(chapter_data.cleaned_data):
                return render(request,self.template_name,{'form':chapter_data,'error':error_msg})
            else:
                course = Course.objects.get(slug=course_slug)
                Chapter.objects.create(
                    course=course,
                    chapterName = chapter_data.cleaned_data['chapterName'],
                    chapterBody = chapter_data.cleaned_data['chapterBody']
                )
                if chapter_data.cleaned_data['add_more']:
                    url = reverse('addchapter', kwargs={'course_slug': slugify(chapter_data.cleaned_data['course'])})
                    return redirect(url)
                else:
                    url = reverse('addtest',kwargs={'course_slug': slugify(chapter_data.cleaned_data['course'])})
                    return redirect(url)
        else:
           return redirect('teacher_dashboard')
        
class AddTest(AddChapter):
    login_url = '/login/'
    template_name = 'addTest.html'
    model = Test
    form_class = TestForm

    def get(self,request,course_slug=None):
        response = super().get(request, course_slug)
        return response
    
    def post(self,request,course_slug=None):
        test_data = self.form_class(request.POST)
        if test_data.is_valid():
            if test_data.cleaned_data['publish']:
                course = Course.objects.get(slug=course_slug)
                course.published = True
                course.save()
                return redirect('teacher_dashboard')
            
            if error_msg:=test_vlaidate(test_data.cleaned_data):
                print(error_msg)
                return render(request,self.template_name,{'form':test_data,'error':error_msg})
            else:
                create_test(test_data.cleaned_data,course_slug)
                if test_data.cleaned_data['add_more']:
                    url = reverse('addtest', kwargs={'course_slug': slugify(test_data.cleaned_data['course'])})
                    return redirect(url)
            
        return redirect('teacher_dashboard')