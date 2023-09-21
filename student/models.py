from django.db import models
from userlog.models import CustomUser
from userlog.base import UserBaseClass

# Create your models here.
class Student(UserBaseClass):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

class UserPreference(models.Model):
    user = models.OneToOneField(Student,on_delete=models.CASCADE)
    html = models.BooleanField(default=False,null=True)
    css = models.BooleanField(default=False,null=True)
    javascript = models.BooleanField(default=False,null=True)
    python = models.BooleanField(default=False,null=True)
    data_analysis = models.BooleanField(default=False,null=True)
    data_structure_and_algorithms = models.BooleanField(default=False,null=True)
    natural_language_processing = models.BooleanField(default=False,null=True)
    machine_learning = models.BooleanField(default=False,null=True)