from django.db import models
from django.contrib.auth.models import User


class JobSeeker(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	is_jobseeker = models.BooleanField(default=True)

	def __str__(self):
    		return f'{self.user}'

	def save(self, *args, **kwargs):
		super(JobSeeker, self).save(*args, **kwargs)
