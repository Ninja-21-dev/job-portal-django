from django.db import models

from employer.models import Job
from portal.models import User


class JobSeekerProfile(models.Model):
    jobseeker = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    resume = models.FileField(blank=True)
    
    def __str__(self):
        return f'{self.jobseeker} profile'
    

class JobSeekerRequests(models.Model):
    requests = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.requests} requested on {self.job}'
    
    def save(self, *args, **kwargs):
        super(JobSeekerRequests, self).save(*args, **kwargs)


class JobSeekerSaveJob(models.Model):
    saved_job = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_jobs')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.saved_job}'
    
    def save(self, *args, **kwargs):
        super(JobSeekerSaveJob, self).save(*args, **kwargs)