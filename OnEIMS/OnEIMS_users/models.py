from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

""" to make individual piture save properly with profile name"""

def path_and_rename(instance, filename):
    upload_to='images/'
    ext = filename.split('.')[-1]
    #part filename
    if instance.user.username:
        filename = 'User_Profile_picture/{}.{}'.format(instance.user.username, ext)
        return os.path.join(upload_to, filename)

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=150, blank=True)
    
    Profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name='Profile_picture', blank=True)

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_type = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_type, default=student)

    def __str__(self):
        return self.user.username