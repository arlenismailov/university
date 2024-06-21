from rest_framework import viewsets
from .models import (
    AboutUniversity, AboutCollege, Faculty, Lyceum, Professor, Student, Event, EventImage, Library,
    JobTitle, LanguageKnowledge, LaborActivity, Management, Structure, Recruitment,
    Document, Direction, DSC, Сontacts, OtherLinks, Followus
)
from .serializers import (
    AboutUniversitySerializer, AboutCollegeSerializer, FacultySerializer, LyceumSerializer, ProfessorSerializer,
    StudentSerializer, EventSerializer, EventImageSerializer, LibrarySerializer, JobTitleSerializer,
    LanguageKnowledgeSerializer, LaborActivitySerializer, ManagementSerializer, StructureSerializer,
    RecruitmentSerializer, DocumentSerializer, DirectionSerializer, DSCSerializer, OtherLinksSerializer,
    FollowusSerializer, СontactsSerializer
)


class AboutUniversityViewSet(viewsets.ModelViewSet):
    queryset = AboutUniversity.objects.all()
    serializer_class = AboutUniversitySerializer


class AboutCollegeViewSet(viewsets.ModelViewSet):
    queryset = AboutCollege.objects.all()
    serializer_class = AboutCollegeSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class LyceumViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LyceumSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventImageViewSet(viewsets.ModelViewSet):
    queryset = EventImage.objects.all()
    serializer_class = EventImageSerializer


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class JobTitleViewSet(viewsets.ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class LanguageKnowledgeViewSet(viewsets.ModelViewSet):
    queryset = LanguageKnowledge.objects.all()
    serializer_class = LanguageKnowledgeSerializer


class LaborActivityViewSet(viewsets.ModelViewSet):
    queryset = LaborActivity.objects.all()
    serializer_class = LaborActivitySerializer


class ManagementViewSet(viewsets.ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class StructureViewSet(viewsets.ModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer


class RecruitmentViewSet(viewsets.ModelViewSet):
    queryset = Recruitment.objects.all()
    serializer_class = RecruitmentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


'''Об университете бүттү '''
from .models import Numbers, Aboutthecollege, Requirem, Documentation, DSC
from .serializers import NumbersSerializer, AboutthecollegeSerializer, RequiremSerializer, DocumentationSerializer, \
    DSCSerializer


class NumbersViewSet(viewsets.ModelViewSet):
    queryset = Numbers.objects.all()
    serializer_class = NumbersSerializer


class AboutthecollegeViewSet(viewsets.ModelViewSet):
    queryset = Aboutthecollege.objects.all()
    serializer_class = AboutthecollegeSerializer


class RequiremViewSet(viewsets.ModelViewSet):
    queryset = Requirem.objects.all()
    serializer_class = RequiremSerializer


class DocumentationViewSet(viewsets.ModelViewSet):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer


class DSCViewSet(viewsets.ModelViewSet):
    queryset = DSC.objects.all()
    serializer_class = DSCSerializer


class СontactsViewSetr(viewsets.ModelViewSet):
    queryset = Сontacts.objects.all()
    serializer_class = СontactsSerializer


class OtherLinksViewSet(viewsets.ModelViewSet):
    queryset = OtherLinks.objects.all()
    serializer_class = OtherLinksSerializer


class FollowusViewSet(viewsets.ModelViewSet):
    queryset = Followus.objects.all()
    serializer_class = FollowusSerializer


from .models import Link, News
from .serializers import LinkSerializer, NewsSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
