from django import forms

from portal.models import User
from .models import JobSeekerProfile


class JobSeekerProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['full_name', 'email']
    
    def __init__(self, *args, **kwargs):
        super(JobSeekerProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "نام و نام خانوادگی"
        self.fields['email'].label = "ایمیل"

        
class JobSeekerResumeForm(forms.ModelForm):
    
    class Meta:
        model = JobSeekerProfile
        fields = ['resume'] 
    
    def __init__(self, *args, **kwargs):
        super(JobSeekerResumeForm, self).__init__(*args, **kwargs)
        self.fields['resume'].label = "فایل رزومه"
