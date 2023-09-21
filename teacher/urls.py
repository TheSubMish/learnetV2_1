from django.urls import path
from .views import TeacherDashboard

urlpatterns = [
    path('teacher/dashboard/',TeacherDashboard.as_view(),name='teacher_dashboard'),
    path('teacher/dashboard/<str:error>',TeacherDashboard.as_view(),name='teacher_dashboard_error')
]
