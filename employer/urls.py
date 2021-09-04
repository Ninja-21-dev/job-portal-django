from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (employer_home,
                   employer_profile,
                   employer_jobs,
                   employer_create_job,
                   )


urlpatterns = [
    path('home', employer_home , name='employer-home'),
    path('profile/', employer_profile , name='employer-profile'),
    path('jobs/', employer_jobs , name='employer-jobs'),
    path('create/job/', employer_create_job , name='employer-create-job'),
    path('logout/',LogoutView.as_view(), name='logout'),
]