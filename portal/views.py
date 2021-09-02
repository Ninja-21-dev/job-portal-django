from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required

from users.models import JobSeeker
from .forms import CompanyCreationForm
from .models import Company


@login_required
def employer_home(request):
    """ show list of requests by jobseekers on jobs created by employer"""     
    if request.user.jobseeker.is_jobseeker:     
            raise Http404
    return render(request, 'employer/home.html')


@login_required
def employer_profile(request):
    """ 
    create company profile by getting information from employer by
    CompanyCreationForm from Company model.
    """
    if request.user.jobseeker.is_jobseeker:     
            raise Http404
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.employer = request.user
            instance.save()
    form = CompanyCreationForm()
    return render(request, 'employer/profile.html', {'form':form})


@login_required
def employer_jobs(request):
    """ show all jobs published by the employer/company."""
    if request.user.jobseeker.is_jobseeker:     
            raise Http404
    return render(request, 'employer/jobs.html')


@login_required
def employer_create_job(request):
    """ create a job and publishe it to the portal"""
    if request.user.jobseeker.is_jobseeker:     
            raise Http404
    return render(request, 'employer/create_job.html')