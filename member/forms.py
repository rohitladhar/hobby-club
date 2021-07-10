from django import forms
from models import UserLogin

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserLogin
        fields = ('name', 'password')