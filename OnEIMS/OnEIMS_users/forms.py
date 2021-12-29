from django import forms
from django.contrib.auth.models import User
from OnEIMS_users.models import user_profile
from django.contrib.auth.forms import UserCreationForm


class Userform(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        label = (
            'password1', 'password'
            'password2', 'Confirm password'
        )
    
class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required=False)

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_types = [
        (student, 'student'),
        (parent, 'parent'),
    ]
        
    user_type = forms.ChoiceField(required=True, choices=user_types)

    class Meta():
        model = user_profile
        fields = ('bio', 'Profile_pic', 'user_type')