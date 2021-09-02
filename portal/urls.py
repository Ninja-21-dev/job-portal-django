from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (employer_home,
                   employer_profile,
                   employer_jobs,
                   employer_create_job
                   )


urlpatterns = [
    path('', employer_home , name='employer-home'),
    path('employer/profile/', employer_profile , name='employer-profile'),
    path('employer/jobs/', employer_jobs , name='employer-jobs'),
    path('employer/create/job/', employer_create_job , name='employer-create-job'),
    path('logout/',LogoutView.as_view(), name='logout'),
]