from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username', 'email','password1','password2']


'''
class LandlordSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model= User
		fields= ['username','email','password','password2']
	def save(self, commit=True):
		user = super().save(commit=False)
		user.is_landlord = True
		if commit:
			 user.save()
			 return user

class TenantSignUpForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields=['username', 'email','password1','password2']
		@transaction.atomic
		def save(self):
			user = super().save(commit=False)
			user.is_student = True
			user.save()
			return user
			'''