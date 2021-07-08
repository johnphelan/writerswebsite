from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

class BiographyForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['bio']

class AccessCodeForm(forms.Form):
	accesscode = forms.CharField(label='ACCESS CODE', max_length=100)


