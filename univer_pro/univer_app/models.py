from django.db import models
from django.contrib.auth.models import User


class AboutUniversity(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class AboutCollege(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Events(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(verbose_name='подробно')
    date = models.DateTimeField(verbose_name='качан башталат')


class ImagesEvents(models.Model):
    university_image = models.ForeignKey(Events, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/events', null=True, blank=True)


class Library(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField()
