from django import forms

from portal.models import User
from .models import JobSeekerProfile


class JobSeekerProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['full_name', 'email']
        
        
class JobSeekerResumeForm(forms.ModelForm):
    
    class Meta:
        model = JobSeekerProfile
        fields = ['resume'] 