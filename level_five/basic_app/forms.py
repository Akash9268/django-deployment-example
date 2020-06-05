from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User

from basic_app.models import userprofileinfo

class UserForm(ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta(ModelForm):
		model = User
		fields = ("username","email","password")
			
class userprofileinfoForm(ModelForm):
	class Meta():
		model =  userprofileinfo
		fields = ("portfolio_site","profile_pic")