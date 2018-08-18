from django.db import models

# Create your models here.

class PutModel(models.Model):
	firstname = models.CharField(default="", blank=True, null=True, max_length=20)
	lastname = models.CharField(default="", blank=True, null=True, max_length=20)