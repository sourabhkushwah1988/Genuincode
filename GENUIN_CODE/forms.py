from django import forms
from .models import Ragister, Contact, CustomUser, LoginAttempt  #  Update model names here if changed
from .models import LoginAttempt  # make sure this model exists

#  Form 1 - Lead Form (For Home page)
class RagisterForm(forms.ModelForm):
    class Meta:
        model = Ragister  #  Update model if needed
        fields = ['name', 'email', 'phone_number']

    # Custom validation or cleaning logic if needed
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # You can add a custom validation here, e.g., check if email already exists
        return email

#  Form 2 - Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact  #  Update model if needed
        fields = ['name', 'email', 'subject', 'message']

    def clean_message(self):
        message = self.cleaned_data.get('message')
        # Example of custom cleaning
        if len(message) < 10:
            raise forms.ValidationError("Message is too short!")
        return message

#  Form 3 - Signup Form

class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#  Form 4 - Login Form

class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginAttempt
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

from django import forms
from django.contrib.auth.models import User
from .models import Profile  # Assuming you have a Profile model

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']  # Add the fields that you want to update