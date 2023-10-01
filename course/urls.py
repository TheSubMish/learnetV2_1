from django.urls import path
from . import views

urlpatterns = [
    path('teacher/add/course/',views.AddCourse.as_view(),name='addcourse'),
    path('teacher/add/<slug:slug>/chapter/',views.AddChapter.as_view(),name='addchapter'),
    path('teacher/add/<slug:slug>/test/',views.AddTest.as_view(),name='addtest'),
    path('teacher/update/<slug:slug>/course/',views.UpdateCourse.as_view(),name='updatecourse'),
    path('teacher/update/<slug:slug>/chapter/<int:pk>',views.UpdateChapter.as_view(),name='updatechapter'),
    path('teacher/update/<slug:slug>/test/<int:pk>',views.UpdateTest.as_view(),name='updatetest')
]
