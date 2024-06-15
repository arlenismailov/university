# views.py

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'department__name', 'is_approved']


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class AboutUniversityViews(viewsets.ModelViewSet):
    queryset = AboutUniversity.objects.all()
    serializer_class = UniversitySerializer


class AboutCollegeViews(viewsets.ModelViewSet):
    queryset = AboutCollege.objects.all()
    serializer_class = CollegeSerializer


class FacultyViews(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class ProfessorViews(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
