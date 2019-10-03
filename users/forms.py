from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label = "আপনার নাম")
	email = forms.EmailField(label = "আপনার ইমেইল এড্রেস")
	address = forms.CharField(label = "আপনার এলাকা")
	mobile = forms.CharField(label = "মোবাইল নম্বর")
	password1 = forms.CharField(label = "পাসওয়ার্ড দিন",widget=forms.PasswordInput())
	password2 = forms.CharField(label = "পুনরায় পাসওয়ার্ড দিন",widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username','email','password1','password2','address','mobile']
