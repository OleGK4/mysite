from django import forms
from .models import User
from .models import Question
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError


# from .models import Profile

class AddQuestionPic:
    class Meta:
        model = Question
        fields = ('photo')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Адрес электронной почты')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
