from django.contrib import admin
from .models import Job_Application

# Register your models here.
@admin.register(Job_Application)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'company_name', 'status')
    list_filter = ('user','status', 'date')
    search_fields = ('user', 'job_title', 'company_name')