from django import forms
from .models import MyUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']