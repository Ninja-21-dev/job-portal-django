from django.urls import path

from .views import (
    jobseeker_profile,
    request_job,
    jobseeker_requests, 
    save_job,
    jobseeker_saved_jobs,
    cancel_request,
)

urlpatterns = [
    path('profile/', jobseeker_profile, name='jobseeker-profile'),
    path('request/job/<int:id>/', request_job, name='request-job'),
    path('requests/', jobseeker_requests, name='jobseeker-requests'),
    path('save/job/<int:id>/', save_job, name='save-job'),
    path('saved/', jobseeker_saved_jobs, name='saved-jobs'),
    path('cancel/request/<int:id>/',cancel_request, name='cancel-request'),
]
