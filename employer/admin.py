from django.contrib import admin

from .models import Company, Job, JobRequests

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobRequests)