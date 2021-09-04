from django import forms

from .models import Company, Job, Category


class EmployerProfileForm(forms.ModelForm):

    class Meta:
        model = Company
        fields=['category', 'name', 'co_introduction', 'logo', 'link']


class EmployerJobCreationForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = [
            'category', 'title', 'location',
            'experience', 'salary', 'cooperation_type',
            'job_description', 'skills_required',
            'military_service', 'degree', 'gender',
        ]