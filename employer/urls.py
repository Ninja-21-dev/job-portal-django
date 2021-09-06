from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (employer_home,
                   employer_profile,
                   employer_jobs,
                   employer_create_job,
                   accepted_status,
                   hired_status,
                   delete_request,
                   )


urlpatterns = [
    path('home', employer_home , name='employer-home'),
    path('profile/', employer_profile , name='employer-profile'),
    path('jobs/', employer_jobs , name='employer-jobs'),
    path('create/job/', employer_create_job , name='employer-create-job'),
    path('accept/request/<int:id>/', accepted_status, name='accept-status'),
    path('hire/request/<int:id>/', hired_status, name='hire-status'),
    path('delete/request/<int:id>/', delete_request, name='delete-request'),
    path('logout/',LogoutView.as_view(), name='logout'),
    
]