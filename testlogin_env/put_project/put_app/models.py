from django.db import models

# Create your models here.

class PutModel(models.Model):
	put_id = models.AutoField(primary_key=True, blank=True, default=1)
	firstname = models.CharField(default="", blank=True, null=True, max_length=20)
	lastname = models.CharField(default="", blank=True, null=True, max_length=20)