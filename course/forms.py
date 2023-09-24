from django import forms

from .models import Course,cousreCategory,Chapter,Test

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['teacher','slug']

    courseTitle = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter Your Course Name'}),required=False)
    courseDescrip = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Your Course Description'}),required=False)
    category = forms.ChoiceField(required=False,choices=cousreCategory,label='Select Category Of Cousre')
    courseImage = forms.ImageField(required=False,label='Course Image')

class ChapterForm(forms.ModelForm):
    course = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Course Name'}))

    class Meta:
        model = Chapter
        fields = '__all__'
        exclude = ['course']

    chapterName = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Chapter Name'}))
    chapterBody = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder':'Enter Chapter Content'}))
    add_more = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=False)
    next = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=False)

class TestForm(forms.ModelForm):
    course = forms.CharField(max_length=50,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Course Name'}))

    class Meta:
        model = Test
        fields = '__all__'
        exclude = ['course']

    title = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Test Title'}))
    question = forms.CharField(max_length=200,required=False,widget=forms.TextInput(attrs={'placeholder':'Test Question'}))
    option1 = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Option One'}))
    option2 = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Option Two'}))
    option3 = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Option Three'}))
    option4 = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Option Four'}))
    corAns = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Enter Correct Answer'}))
    add_more = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=False)
    publish = forms.BooleanField(required=False, widget=forms.HiddenInput(), initial=False)