from django.db import models
from django.contrib.auth.models import User

''' 3 зоведение с низу '''


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


class Lyceum(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Faculty(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


''' пользователи '''


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


class StudentNumber(models.Model):
    number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.number


'''Событие'''


class Event(models.Model):  # Событие
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name='Подробно')
    date = models.DateTimeField(verbose_name='Дата и время начала')

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/events', null=True, blank=True)


'''Библиотека'''


class Library(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    description = models.TextField()

    def __str__(self):
        return self.title


'''О себе'''


class JobTitle(models.Model):
    date_of_birth = models.CharField(max_length=100, verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=100, verbose_name='Место рождения')
    nationality = models.CharField(max_length=100, verbose_name='Национальность')

    def __str__(self):
        return f"{self.date_of_birth} - {self.place_of_birth} - {self.nationality}"


class LanguageKnowledge(models.Model):
    language = models.CharField(max_length=100, verbose_name='Язык')
    level = models.CharField(max_length=100,
                             verbose_name='Уровень владения')  # Например, начальный, средний, продвинутый

    def __str__(self):
        return self.language


class LaborActivity(models.Model):
    activity = models.TextField(verbose_name='Трудовая деятельность')

    def __str__(self):
        return self.activity


class Management(models.Model):  # Руководство
    job_title = models.CharField(max_length=100, verbose_name='Должность')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    img = models.ImageField(upload_to='management/img', verbose_name='Фото')
    job_info = models.ForeignKey(JobTitle, on_delete=models.CASCADE, verbose_name='О себе')
    academic_title_and_position = models.CharField(max_length=100, verbose_name='Учёное звание и должность')
    education = models.TextField(verbose_name='Образование')
    labor_activities = models.ManyToManyField(LaborActivity, verbose_name='Трудовая деятельность')
    language_knowledge = models.ManyToManyField(LanguageKnowledge, verbose_name='Знание языков')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return self.full_name


class Structure(models.Model):  # Структура
    description = models.TextField(verbose_name='Описание структуры')
    img = models.ImageField(upload_to='structure/img')

    def __str__(self):
        return self.description[:50]


'''Направления и специализации университета'''


class Recruitment(models.Model):  # Осуществляется набор по следующим направлениям:
    title = models.TextField(verbose_name='Осуществляется набор по следующим направлениям:')

    def __str__(self):
        return self.title[:50]


class Document(models.Model):  # Документы, необходимые для поступления:
    title = models.CharField(max_length=200, verbose_name='Документы, необходимые для поступления:')

    def __str__(self):
        return self.title


class Direction(models.Model):
    recruitments = models.ManyToManyField(Recruitment, verbose_name='Осуществляется набор по следующим направлениям:')
    documents = models.ManyToManyField(Document, verbose_name='Документы, необходимые для поступления:')

    def __str__(self):
        # Возвращаем первые несколько направлений для краткости
        recruitments_titles = ", ".join([recruitment.title[:50] for recruitment in self.recruitments.all()[:3]])
        return f"Direction with recruitments: {recruitments_titles}..."


'''Об университете бүттү '''


class Numbers(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Aboutthecollege(models.Model):  # Направления и специализации Колледжа
    kit = models.CharField(max_length=100, verbose_name='набор')
    numbers = models.ManyToManyField(Numbers, verbose_name='numbers and text')

    def __str__(self):
        return self.kit


class Requirem(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Documentation(models.Model):
    title = models.CharField(max_length=100)
    requirem = models.ManyToManyField(Requirem, verbose_name='требования')

    def __str__(self):
        return self.title


class DSC(models.Model):  # Направления и специализации колледжа
    aboutthecollege = models.ForeignKey(Aboutthecollege, on_delete=models.CASCADE)
    documentation = models.ForeignKey(Documentation, on_delete=models.CASCADE)

    def __str__(self):
        return f"DSC for {self.aboutthecollege.kit} and {self.documentation.title}"


'''КОНТАКТЫ'''


class Number(models.Model):
    numbers = models.ImageField()


class Сontacts(models.Model):
    address = models.CharField(max_length=50)
    numbers = models.ManyToManyField(Number, verbose_name='контакты')
    link = models.URLField(verbose_name='e-mail')


'''Другие ссылки'''


class OtherLinks(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название ссылки', null=True, blank=True)
    link = models.URLField(null=True, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title


class Followus(models.Model): #  Следите за нами:
    link = models.URLField(null=True, blank=True, verbose_name='Следите за нами:')


'''НПА'''


class Link(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    pdf = models.FileField(upload_to='links/pdf/', null=True, blank=True)  # Added field for PDF files

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='news/img/', null=True, blank=True)
    video = models.FileField(upload_to='news/video/', null=True, blank=True)
    pdf = models.FileField(upload_to='news/pdf/', null=True, blank=True)
    link = models.ManyToManyField(Link, verbose_name='link', blank=True)  # Removed max_length
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
