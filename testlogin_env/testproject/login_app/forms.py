from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={
		'class': 'form-control expnd dynamic-font reg-col-input-in',
		'placeholder': 'Enter password',

	}))

	class Meta():
		model = User
		fields = ('username', 'password')
		widgets = {
			'username': forms.TextInput(attrs = {
				'class': 'form-control expnd dynamic-font reg-col-input-in',
				'placeholder': 'Enter username',
			}),
		}


class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('profile_pic',)
	

