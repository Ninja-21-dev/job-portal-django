from datetime import datetime, timezone

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import Http404

from employer.models import Job
from .forms import UserRegisterForm, UserLoginForm
from .models import JobSeeker, User


def home_page(request):
    jobs = Job.objects.all()
    # convert time
    now = datetime.now(timezone.utc)
    for i in jobs:
        get_days = now - i.created_date
        if get_days.days > 1:
            i.created_date = f'{get_days.days} روز پیش' 
    return render(request, 'home_page.html', {'jobs':jobs})


def employer_register(request):
    if request.user.is_authenticated:
            raise Http404
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                    data['email'],
                    data['full_name'],
                    data['password1'],
                    )
            role = JobSeeker(is_jobseeker=False, user=user)
            role.save()
            messages.success(
                request, 'ثبت نام انجام شد - از طریق فرم زیر وارد شوید'
                )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'employer/register.html', {'form':form})


def jobseeker_register(request):
    if request.user.is_authenticated:
            raise Http404
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                    data['email'],
                    data['full_name'],
                    data['password1'],
                    )
            user.save()
            role = JobSeeker(is_jobseeker=True, user=user)
            role.save()
            messages.success(
                request, 'ثبت نام انجام شد - از طریق فرم زیر وارد شوید'
                )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'jobseeker/register.html', {'form':form})


def login_request(request):
    if request.user.is_authenticated:
        raise Http404
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, email=data['email'], password=data['password']
                )
            if user is not None:
                login(request, user)
                # if user is jobseeker
                if user.jobseeker.is_jobseeker:
                    return redirect('jobseeker-home')
                # if user is a employer
                elif not user.jobseeker.is_jobseeker:
                    return redirect('employer-home')
            else:
                messages.success(request, 'نام کاربری با رمز عبور صحیح نیست')
                return redirect('login')
    form = UserLoginForm()
    return render(request, 'login.html', {'form':form})
