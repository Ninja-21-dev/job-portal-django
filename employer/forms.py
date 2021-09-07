from django import forms

from .models import Company, Job, Category


class EmployerProfileForm(forms.ModelForm):

    class Meta:
        model = Company
        fields=['category', 'name', 'co_introduction', 'logo', 'link']

    def __init__(self, *args, **kwargs):
        super(EmployerProfileForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "دسته بندی شرکت خود را انتخاب کنید"
        self.fields['name'].label = "نام شرکت خود را وارد کنید"
        self.fields['co_introduction'].label = "شرکت خود را معرفی کنید"
        self.fields['logo'].label = "لوگوی خود را آپلود کنید"
        self.fields['link'].label = "لینک وبسایت خود را وارد کنید"

class EmployerJobCreationForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = [
            'category', 'title', 'location',
            'experience', 'salary', 'cooperation_type',
            'job_description', 'skills_required',
            'military_service', 'degree', 'gender',
        ]
    
    def __init__(self, *args, **kwargs):
        super(EmployerJobCreationForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "دسته بندی آگهی خود را انتخاب کنید"
        self.fields['title'].label = "عنوان آگهی را وارد کنید"
        self.fields['location'].label = "موقعیت مکانی شرکت را وارد کنید"
        self.fields['experience'].label = "سابقه کار مورد نیاز"
        self.fields['salary'].label = "حقوق پرداختی"
        self.fields['cooperation_type'].label = "نوع همکاری"
        self.fields['job_description'].label = "شرح موقعیت شغلی"
        self.fields['skills_required'].label = "مهارت های مورد نیاز"
        self.fields['military_service'].label = "وضعیت سربازی"
        self.fields['gender'].label = "جنسیت"
        self.fields['degree'].label = "تحصیلات"



