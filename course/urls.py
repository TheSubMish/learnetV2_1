from django.urls import path
from . import views

urlpatterns = [
    path('teacher/add/course/',views.AddCourse.as_view(),name='addcourse'),
    path('teacher/add/<slug:course_slug>/chapter/',views.AddChapter.as_view(),name='addchapter'),
    path('teacher/add/<slug:course_slug>/test/',views.AddTest.as_view(),name='addtest')
]
