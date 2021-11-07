from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpUserForm(UserCreationForm):
    # username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
    #     attrs={'placeholder': 'Somchai'}))
    # email = forms.EmailField(max_length=250, widget=forms.EmailInput(
    #     attrs={'placeholder': 'example@gmail.com'}))
    # password1 = forms.CharField(label='Password',
    #                             widget=forms.PasswordInput(attrs={'placeholder': '123456example'}))
    # password2 = forms.CharField(label='Confirm password',
    #                             widget=forms.PasswordInput(attrs={'placeholder': '123456example'}))

    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, required=True)
    password1 = forms.CharField(min_length=6, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',
                  'email', 'password1', 'password2')
