from django.contrib import admin

from .models import Company, Job, Category

admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Category)