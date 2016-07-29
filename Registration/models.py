from django.db import models

# Create your models here.
class Registration(models.Model):
    account_name = models.CharField(max_length=100)
    manager_first = models.CharField(max_length=200)
    manager_last = models.CharField(max_length=200)
    manager_email = models.CharField(max_length=200)
    manager_phone = models.CharField(max_length=10)
