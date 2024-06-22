from rest_framework import serializers
from .models import Student, Library, AboutUniversity, AboutCollege, Faculty, Professor
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')

    class Meta:
        model = Student
        fields = ['user', 'user_id', 'department', 'enrollment_date', 'graduation_date', 'is_approved']


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['title', 'pdf', 'description']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUniversity
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCollege
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
