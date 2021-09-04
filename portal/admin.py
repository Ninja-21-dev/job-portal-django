from django.contrib import admin

from .models import JobSeeker, User, Category

admin.site.register(JobSeeker)
admin.site.register(User)
admin.site.register(Category)