from django.db import models
from django.utils import timezone
from django_jalali.db import models as jmodels

from PIL import Image

from portal.models import JobSeeker, User, Category


class Company(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    co_introduction = models.TextField()
    logo = models.ImageField(default='default.png', upload_to='co-logo')
    link  = models.CharField(max_length=80)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super(Company, self).save(*args, **kwargs)

        img = Image.open(self.logo.path)


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=timezone.now)
    experience_choices = (
        ('no-matter','مهم نیست'),
        ('1-3', 'یک تا ۳ سال'),
        ('3-6', 'سه تا ۶ سال'),
        ('+6', 'بیشتر از ۶ سال'),
    )
    experience = models.CharField(max_length=80, choices=experience_choices)
    salary_choices = (
        ('agreement ', 'توافقی'),
        ('from 3', 'از ۳ میلیون'),
        ('from 5', 'از ۵ میلیون'),
        ('from 8', 'از ۸ میلیون'),
        ('from 10', 'از ۱۰ میلیون'),
        ('from 12', 'از ۱۲ میلیون'),
        ('from 15', 'از ۱۵ میلیون'),
    )
    salary = models.CharField(
        max_length=80, choices=salary_choices
    )
    cooperation_choices = (
        ('full-time', 'تمام وقت'),
        ('part-time', 'پاره وقت'),
        ('remote', 'دور کاری'),
        ('internship', 'کار آموزی'),
    )
    cooperation_type = models.CharField(
        max_length=80, choices=cooperation_choices
    )
    job_description = models.TextField()
    skills_required = models.CharField(max_length=80)
    military_choices = (
        ('no-matter', 'مهم نیست'),
        ('end', 'پایان خدمت'),
    )
    military_service = models.CharField(
        max_length=80, choices=military_choices
    )
    degree_choices = (
        ('no-matter', 'مهم نیست'),
        ('diploma', 'دیپلم'),
        ('bachelor', 'لیسانس'),
    )
    degree = models.CharField(max_length=80, choices=degree_choices)
    gender_choices = (
        ('Male', 'مرد'),
        ('Female', 'زن'),
        ('not-matter','مهم نیست'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices)

    def __str__(self):
        return self.title