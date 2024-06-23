from rest_framework import serializers
from .models import (
    AboutUniversity, AboutCollege, Faculty, Lyceum, Student, Student, Event, EventImage, Library,
    JobTitle, LanguageKnowledge, LaborActivity, Management, Structure, Recruitment,
    Document, Direction, Numbers, Aboutthecollege, Requirem, Documentation, Сontacts, OtherLinks, Followus,
    Link, News, Numbers, Aboutthecollege, Requirem, Documentation, DSC
)


class AboutUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUniversity
        fields = '__all__'


class AboutCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCollege
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class LyceumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyceum
        fields = '__all__'


from rest_framework import serializers
from .models import Student


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['student_id']


class VerifyCodeSerializer(serializers.Serializer):
    student_id = serializers.IntegerField()
    verification_code = serializers.CharField(max_length=6)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ['date_of_birth', 'place_of_birth', 'nationality']


class LanguageKnowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageKnowledge
        fields = ['language', 'level']


class LaborActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaborActivity
        fields = ['activity']


class ManagementSerializer(serializers.ModelSerializer):
    job_info = JobTitleSerializer()
    labor_activities = LaborActivitySerializer(many=True)
    language_knowledge = LanguageKnowledgeSerializer(many=True)

    class Meta:
        model = Management
        fields = ['id', 'job_title', 'full_name', 'img', 'academic_title_and_position', 'education', 'job_info',
                  'labor_activities', 'language_knowledge', 'create']


class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = '__all__'


class RecruitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitment
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'


'''Об университете бүттү '''


class NumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numbers
        fields = ['title']


class AboutthecollegeSerializer(serializers.ModelSerializer):
    numbers = NumbersSerializer(many=True)

    class Meta:
        model = Aboutthecollege
        fields = ['kit', 'numbers']


class RequiremSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirem
        fields = ['title']


class DocumentationSerializer(serializers.ModelSerializer):
    requirem = RequiremSerializer(many=True)

    class Meta:
        model = Documentation
        fields = ['title', 'requirem']


class DSCSerializer(serializers.ModelSerializer):
    aboutthecollege = AboutthecollegeSerializer()
    documentation = DocumentationSerializer()

    class Meta:
        model = DSC
        fields = ['aboutthecollege', 'documentation']


class СontactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сontacts
        fields = ['id', 'address', 'numbers', 'link']


class OtherLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherLinks
        fields = ['id', 'title', 'link']


class FollowusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followus
        fields = ['id', 'link']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    link = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'
