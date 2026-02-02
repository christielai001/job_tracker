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
        queryset = Job_Application.objects.filter(user=self.request.user)

        date = self.request.query_params.get('date')
        job_title = self.request.query_params.get('job_title')
        company_name = self.request.query_params.get('company_name')
        status = self.request.query_params.get('status')
        location = self.request.query_params.get('location')
        salary_min = self.request.query_params.get('salary_min')
        salary_max = self.request.query_params.get('salary_max')

        if date:
            queryset = queryset.filter(date=date)

        if job_title:
            queryset = queryset.filter(job_title__icontains=job_title)

        if company_name:
            queryset = queryset.filter(company_name__icontains=company_name)

        if status:
            queryset = queryset.filter(status=status)
        
        if location:
            queryset = queryset.filter(location__icontains=location)
        
        # gte = greater than or equal to
        if salary_min:
            queryset = queryset.filter(salary_min__gte=salary_min) 

        # lte = less than or equal to
        if salary_max:
            queryset = queryset.filter(salary_max__lte=salary_max)
            
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)