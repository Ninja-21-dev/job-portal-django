from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm
from .models import JobSeeker, User


def employer_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = User.objects.create_user(
       				data['email'],
           			data['full_name'],
					data['password1'],
					data['password2']
     		)
			login(request, user)
			role = JobSeeker(is_jobseeker=False, user=user)
			role.save()
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'employer_register.html', {'form':form})



def jobseeker_register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = User.objects.create_user(
       				data['email'],
           			data['full_name'],
					data['password1'],
					data['password2']
     		)
			user.save()
			role = JobSeeker(is_jobseeker=True, user=user)
			role.save()
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user_register.html', {'form':form})


def login_request(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request, email=data['email'], password=data['password'])
			if user is not None:
				login(request, user)
				if user.jobseeker.is_jobseeker:
					messages.success(request,f'Account Created, You are ready to login')
					return redirect('employer-homehome')
				else:
					messages.success(request,f'Account Created, You are ready to login')
					return redirect('employer-home')
			else:
				messages.success(request, 'invalid username or password')
				return redirect('login')
		else:
			messages.success(request, 'invalid username or password')
			return redirect('login')
	else:
		form = UserLoginForm()
	return render(request, 'login.html', {'form':form})
