from django.db import models

from employer.models import Job
from portal.models import User


class JobSeekerProfile(models.Model):
    jobseeker = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField()
    
    def __str__(self):
        return f'{self.jobseeker} profile'
    

class JobSeekerRequests(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    requests = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE, related_name='requests')
    
    def __str__(self):
        return f'{self.requests} requested on {self.job}'
    
    def save(self, *args, **kwargs):
        super(JobSeekerRequests, self).save(*args, **kwargs)


class JobSeekerSaveJob(models.Model):
    job = models.OneToOneField(Job, on_delete=models.CASCADE)
    saved_job = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE,  related_name='saved')
    
    def __str__(self):
        return f'{self.favorites} favorite'
    
    def save(self, *args, **kwargs):
        super(JobSeekerSaveJob, self).save(*args, **kwargs)