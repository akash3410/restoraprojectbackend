from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': "Username", 'class': 'form-control'})
    )
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={'placeholder': "First Name", 'class': 'form-control'})
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={'placeholder': "Last Name", 'class': 'form-control'})
    )
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': "Valid Email", 'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': "Password", 'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': "Confirm Password", 'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': "Username", 'class': 'form-control'})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': "Password", 'class': 'form-control'})
    )