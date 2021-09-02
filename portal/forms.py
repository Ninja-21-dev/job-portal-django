from django import forms

from .models import Company, Job, Category

class CompanyCreationForm(forms.ModelForm):

    class Meta:
        model = Company
        fields=['category', 'name', 'co_introduction', 'logo', 'link']
