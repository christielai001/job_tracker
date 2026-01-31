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
# automatically provides all CRUD endpoints
class Job_ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = Job_ApplicationSerializer

    def get_queryset(self):
        return Job_Application.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)