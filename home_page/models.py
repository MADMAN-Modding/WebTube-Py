from django.db import models

class HomePage(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)