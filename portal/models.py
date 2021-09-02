from django.db import models

from PIL import Image

from users.models import JobSeeker, User


class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
       return self.name


class Company(models.Model):
    employer = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    co_introduction = models.TextField()
    logo = models.ImageField(default='default.jpg', upload_to='company_logo')
    link  = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Job(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    location = models.CharField(max_length=80)
    experience_choices = (
        ('no-matter','مهم نیست'),
        ('1-3', 'یک تا ۳ سال'),
        ('3-6', 'سه تا ۶ سال'),
        ('+6', 'بیشتر از ۶ سال'),
    )
    experience = models.CharField(max_length=80, choices=experience_choices)
    salary = models.IntegerField()
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