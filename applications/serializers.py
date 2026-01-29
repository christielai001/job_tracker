from rest_framework import serializers
from .models import Job_Application


class Job_ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Application
        fields = '__all__'