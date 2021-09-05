from django.contrib import admin

from .models import JobSeekerProfile, JobSeekerRequests, JobSeekerSaveJob

admin.site.register(JobSeekerProfile)
admin.site.register(JobSeekerRequests)
admin.site.register(JobSeekerSaveJob)