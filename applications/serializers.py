from rest_framework import serializers
from .models import Job_Application

# renders data to JSON or other types for API responses 
class Job_ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Application
        fields = '__all__'