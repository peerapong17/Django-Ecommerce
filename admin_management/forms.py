from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpAdminForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, required=True)
    password1 = forms.CharField(min_length=6, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                  'email', 'password1', 'password2')
