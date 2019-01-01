from django.db import models

class UserProfileInfo(models.Model):
	username = models.CharField(max_length=15, blank=True, null=True, default="dude")
	password = models.CharField(max_length=15, blank=True, null=True, default="dude")
