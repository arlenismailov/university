# univer_app/admin.py

from django.contrib import admin
from .models import AboutUniversity, AboutCollege, Faculty, Professor, Student, Events, ImagesEvents, Library


@admin.register(AboutUniversity)
class AboutUniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(AboutCollege)
class AboutCollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'title', 'bio']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'department', 'enrollment_date', 'graduation_date']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date']


@admin.register(ImagesEvents)
class ImagesEventsAdmin(admin.ModelAdmin):
    list_display = ['university_image', 'image']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['title', 'pdf', 'description']
