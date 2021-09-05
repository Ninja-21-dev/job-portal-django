from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.http import Http404

from .forms import JobSeekerProfileForm, JobSeekerResumeForm
from .models import JobSeekerProfile, JobSeekerRequests, JobSeekerSaveJob
from employer.models import Job, JobRequests


def is_jobseeker(user):
    try:
        if not user.usertype.is_jobseeker:
            raise Http404
        return True
    except:
        raise Http404


@user_passes_test(is_jobseeker)
@login_required
def jobseeker_profile(request):
    if request.method == 'POST':   
        profile_form = JobSeekerProfileForm(request.POST, instance=request.user)
        resume_form = JobSeekerResumeForm(request.POST,
                                          request.FILES,
                                          instance=request.user.jobseekerprofile)
        if profile_form.is_valid() and resume_form.is_valid():
            profile_form.save()
            resume_form.save()
            messages.success(request, 'پروفایل شما به روز شد')
            return redirect('jobseeker-profile')
    
    else: 
        profile_form = JobSeekerProfileForm(instance=request.user)
        resume_form = JobSeekerResumeForm(instance=request.user.jobseekerprofile)
    
    context = {
        'profile_form' : profile_form,
        'resume_form' : resume_form,
    }
    return render(request, 'jobseeker_profile.html', context)


@user_passes_test(is_jobseeker)
@login_required
def request_job(request, id):
    if request.user.jobseekerprofile.requests.filter(job=id):
        messages.success(request, ' هم اکنون برای این آگهی رزومه ارسال کرده اید')
        return redirect('home-page')
    job = Job.objects.filter(id=id).first()
    req = JobSeekerRequests(job=job, requests=request.user.jobseekerprofile)
    req.save()
    req_to_employer = JobRequests(
        jobseeker=request.user,
        job=job,
        resume_url=request.user.jobseekerprofile.resume.url,
        employer=job.company,
        )
    req_to_employer.save()
    messages.success(request, 'رزومه شما ارسال شد')
    return redirect('home-page')


@user_passes_test(is_jobseeker)
@login_required
def jobseeker_requests(request):
    requests = request.user.jobseekerprofile.requests.all()
    return render(request, 'jobseeker_requests.html', {'requests':requests})


@user_passes_test(is_jobseeker)
@login_required
def save_job(request, id):
    if request.user.jobseekerprofile.saved.filter(job=id):
        messages.success(request, 'این آگهی قبلا ذخیره شده')
        return redirect('home-page')
    job = Job.objects.filter(id=id).first()
    save_job = JobSeekerSaveJob(job=job, saved_job=request.user.jobseekerprofile)
    save_job.save()
    messages.success(request, 'این آگهی ‌ذخیره شد')
    return redirect('home-page')


@user_passes_test(is_jobseeker)
@login_required
def jobseeker_saved_jobs(request):
    jobs = request.user.jobseekerprofile.saved.all()
    return render(request, 'jobseeker_saved_jobs.html', {'jobs':jobs})