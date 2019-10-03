from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile
# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			new_profile = Profile(
				user= request.user,
				address = request.POST['address'],
				mobile = request.POST['mobile']
				)
			new_profile.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'{username} আপনার একাউন্ট তৈরি হয়ে গেছে। এখন লগইন করুন !')
			return redirect('login')
	else:
		form = UserRegisterForm()

	return render(request,'users/register.html',{'forms':form})


@login_required
def profile(request):
	return render(request,'users/profile.html')
