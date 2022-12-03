from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import UserTable

class UserForm(ModelForm):
    class Meta:
        model = UserTable
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'date_joined', 'email', 'password1', 'password2']
