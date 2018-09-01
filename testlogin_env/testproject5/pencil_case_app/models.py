from django.db import models

# Create your models here.

class PencilCase(models.Model):
	pencil = models.CharField(default="", blank=True, null=True, max_length=15)
	rubber = models.CharField(default="", blank=True, null=True, max_length=15)
	pen = models.CharField(default="", blank=True, null=True, max_length=15)
