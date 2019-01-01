from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')'username': forms.TextInput(attrs={'placeholder': 'username'}),'username': forms.TextInput(attrs={'placeholder': 'username'}),zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
