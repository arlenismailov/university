from django.contrib import admin
from .models import (
    AboutUniversity, AboutCollege, Faculty, Student, Event, EventImage, Library,
    JobTitle, LanguageKnowledge, LaborActivity, Management, Structure, Recruitment,
    Document, Direction, DSC, OtherLinks, Сontacts, Followus, Link, News
)

admin.site.register(AboutUniversity)
admin.site.register(AboutCollege)
admin.site.register(Faculty)
admin.site.register(Student)
''' низу 2 класса для фото события '''


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


@admin.register(Event)
class PhotoEvent(admin.ModelAdmin):
    inlines = [EventImageInline]


admin.site.register(Library)
admin.site.register(JobTitle)
admin.site.register(LanguageKnowledge)
admin.site.register(LaborActivity)
admin.site.register(Management)
admin.site.register(Structure)
admin.site.register(Recruitment)
admin.site.register(Document)
admin.site.register(Direction)
admin.site.register(DSC)
admin.site.register(Сontacts)
admin.site.register(OtherLinks)
admin.site.register(Followus)

admin.site.register(Link)
admin.site.register(News)