from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import Job_ApplicationSerializer
from .models import Job_Application

# health check
@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})

# Create your views here.
class Job_ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Job_Application.objects.all()
    serializer_class = Job_ApplicationSerializer