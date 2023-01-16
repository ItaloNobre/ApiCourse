from django.shortcuts import render
from rest_framework import viewsets
from .models import Course, Assessment
from .serializers import CourseSerializer,AssessmentSerializer



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer