from django.contrib import admin

from .models import JobSeeker, User

admin.site.register(JobSeeker)
admin.site.register(User)