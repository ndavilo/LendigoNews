from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import PasswordInput
from news.models import Profile

class SignUpForm(UserCreationForm):
	email 		=	forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name	=	forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})) 
	last_name	=	forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model 	=	User
		fields 	=	('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__ (self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditSettingsForm(UserChangeForm):
	email 		=	forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name	=	forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'})) 
	last_name	=	forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password 	=	forms.CharField(required=False, max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Click on Change password bellow'}))



	class Meta:
		model 	=	User
		fields 	=	('first_name', 'last_name', 'email')

class PasswordChangingForm(PasswordChangeForm):
	old_password 		=	forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
	new_password1		=	forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'})) 
	new_password2		=	forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

	class Meta:
		model 	=	User
		fields 	=	('old_password', 'new_password1', 'new_password2')

class ProfilePageForm(forms.ModelForm):
	class Meta:
		model 		=	Profile
		fields 		=	('Phone', 'bio', 'profile_pic')
		widgets 	=	{
				'Phone'			:	forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Phone Number'}),
				'bio'			:	forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About Yourself'}),
				'profile_pic'	:	forms.Textarea(attrs={'class': 'form-control'}),
		}










	