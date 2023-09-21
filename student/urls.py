from django.urls import path

from .views import StudentDashboard

urlpatterns = [
    path('student/dashboard/',StudentDashboard.as_view(),name='student_dashboard'),
    path('student/dashboard/<str:error>',StudentDashboard.as_view(),name='student_dashboard_error')
]