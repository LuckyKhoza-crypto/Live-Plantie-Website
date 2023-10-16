from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2')
        model = get_user_model() #imports the user information quickly
