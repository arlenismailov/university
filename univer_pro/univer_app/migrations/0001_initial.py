# Generated by Django 5.0.6 on 2024-06-22 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Aboutthecollege',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit', models.CharField(max_length=100, verbose_name='набор')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('name_tr', models.CharField(max_length=20, null=True)),
                ('name_en', models.CharField(max_length=20, null=True)),
                ('description', models.TextField()),
                ('description_tr', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Документы, необходимые для поступления:')),
            ],
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(verbose_name='Подробно')),
                ('date', models.DateTimeField(verbose_name='Дата и время начала')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Followus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Следите за нами:')),
            ],
        ),
        migrations.CreateModel(
            name='JobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.CharField(max_length=100, verbose_name='Дата рождения')),
                ('place_of_birth', models.CharField(max_length=100, verbose_name='Место рождения')),
                ('nationality', models.CharField(max_length=100, verbose_name='Национальность')),
            ],
        ),
        migrations.CreateModel(
            name='LaborActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.TextField(verbose_name='Трудовая деятельность')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageKnowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100, verbose_name='Язык')),
                ('level', models.CharField(max_length=100, verbose_name='Уровень владения')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='pdfs/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='links/pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='Lyceum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OtherLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название ссылки')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Осуществляется набор по следующим направлениям:')),
            ],
        ),
        migrations.CreateModel(
            name='Requirem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание структуры')),
                ('img', models.ImageField(upload_to='structure/img')),
            ],
        ),
        migrations.CreateModel(
            name='DSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutthecollege', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer_app.aboutthecollege')),
                ('documentation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer_app.documentation')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/events')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='univer_app.event')),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100, verbose_name='Должность')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('img', models.ImageField(upload_to='management/img', verbose_name='Фото')),
                ('academic_title_and_position', models.CharField(max_length=100, verbose_name='Учёное звание и должность')),
                ('education', models.TextField(verbose_name='Образование')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('job_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer_app.jobtitle', verbose_name='О себе')),
                ('labor_activities', models.ManyToManyField(to='univer_app.laboractivity', verbose_name='Трудовая деятельность')),
                ('language_knowledge', models.ManyToManyField(to='univer_app.languageknowledge', verbose_name='Знание языков')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='news/img/')),
                ('video', models.FileField(blank=True, null=True, upload_to='news/video/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='news/pdf/')),
                ('create', models.DateField(auto_now_add=True)),
                ('link', models.ManyToManyField(blank=True, to='univer_app.link', verbose_name='link')),
            ],
        ),
        migrations.AddField(
            model_name='aboutthecollege',
            name='numbers',
            field=models.ManyToManyField(to='univer_app.numbers', verbose_name='numbers and text'),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer_app.faculty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.ManyToManyField(to='univer_app.document', verbose_name='Документы, необходимые для поступления:')),
                ('recruitments', models.ManyToManyField(to='univer_app.recruitment', verbose_name='Осуществляется набор по следующим направлениям:')),
            ],
        ),
        migrations.AddField(
            model_name='documentation',
            name='requirem',
            field=models.ManyToManyField(to='univer_app.requirem', verbose_name='требования'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('graduation_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='univer_app.faculty')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Сontacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('link', models.URLField(verbose_name='e-mail')),
                ('numbers', models.ManyToManyField(to='univer_app.number', verbose_name='контакты')),
            ],
        ),
    ]
