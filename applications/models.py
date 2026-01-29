from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms

# Create your models here.
class Job_Application(models.Model):

    status_choices = [
        ("applied", "Applied"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    job_title = models.CharField(max_length=1000)
    company_name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    salary = models.IntegerField()
    status = models.CharField(max_length=25, choices=status_choices, default='applied')

    def __str__(self):
        return f'{self.date} : {self.job_title}'