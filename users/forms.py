from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Social

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


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
		fields = ['bio', 'instagram', 'twitter', 'facebook', 'linkedin']

class AccessCodeForm(forms.Form):
	accesscode = forms.CharField(label='ACCESS CODE', max_length=100)

class SocialForm(forms.Form):

	class Meta:
		model = Social
		fields = ['']


