from datetime import datetime, timezone

from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .forms import EmployerJobCreationForm, EmployerProfileForm
from .models import Company, UserType, JobRequests


def is_employer(user):
    try:
        if user.usertype.is_jobseeker:
            raise Http404
        return True
    except:
        raise Http404


@user_passes_test(is_employer)
@login_required
def employer_home(request):
    """
    show list of requests by jobseekers on jobs created by employer
    ------------------
    when user logged in for first ever; right after the registeration
    the exception happens because user/employer has not profile yet.
    in this case we redirect user to employer_profile() to make the profile.
    """     
    try:
        requests = JobRequests.objects.filter(employer=request.user.company)
    except Company.DoesNotExist:
        messages.success(request, 'برای دسترسی به بخش های دیگر ابتدا اطلاعات زیر را تکمیل کنید')
        return redirect('employer-profile')
        
    return render(request, 'employer_home.html', {'requests':requests, 'range':range(len(requests))})


@user_passes_test(is_employer)
@login_required
def employer_profile(request):
    """ 
    Company Profile
    request.user = employer
    -----------------------
    when a user registered and logged in for first ever time;
    to let the employer create a job we need their information.
    so step-1 is to complete their profile - actually we create a company profile.
    that case handles in the exception;
    when the "RelatedObject.DoesNotExist" error appears.
    otherwise when employer already has a profile, form shows the information
    from database and employer can update their informations.
    """
    try: # if user already has a profile show their information in form 
        if request.method == 'POST':
            form = EmployerProfileForm(
                request.POST, request.FILES, instance=request.user.company
                )
            if form.is_valid():
                instance = form.save(commit=False)
                instance.employer = request.user
                instance.save()
                messages.success(request, 'پروفایل شما به روز رسانی شد')
                return redirect('employer-profile')
        form = EmployerProfileForm(instance=request.user.company)
    except Company.DoesNotExist: 
            # if user is new and has not a profile
            if request.method == 'POST':
                form = EmployerProfileForm(request.POST)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.employer = request.user
                    instance.save()
                    messages.success(request, 'پروفایل شما ایجاد شد')
                    messages.success(
                        request,
                        """
                        برای ایجاد آگهی از منوی بالا گزینه
                        آگهی جدید را انتخاب کنید
                        """
                    )
                    return redirect('employer-profile')
            form = EmployerProfileForm()
    return render(request, 'profile.html', {'form':form})


@user_passes_test(is_employer)
@login_required
def employer_jobs(request):
    """ show all jobs published by the employer/company."""
    try:
        jobs = request.user.company.jobs.all()
        now = datetime.now(timezone.utc)
        for i in jobs:
            get_days = now - i.created_date
            if get_days.days > 1:
                i.created_date = f'{get_days.days} روز پیش' 
        requests = JobRequests.objects.filter(employer=request.user.company)
    except Company.DoesNotExist:
        return redirect('employer-home')
    return render(request, 'jobs.html', {'jobs':jobs, 'number':len(requests)})


@user_passes_test(is_employer)
@login_required
def employer_create_job(request):
    """ create a job and publishe it to the portal"""
    try:
        if request.method == 'POST':
            form = EmployerJobCreationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.company = request.user.company
                instance.save() 
        elif request.method == 'GET':
            form = EmployerJobCreationForm()
    except Company.DoesNotExist:
        raise Http404
    return render(request, 'create_job.html', {'form':form})