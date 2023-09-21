from django.contrib import admin
from .models import Student,UserPreference
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(Student,StudentAdmin)

class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ['user']
admin.site.register(UserPreference,UserPreferenceAdmin)