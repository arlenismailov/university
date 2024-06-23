from rest_framework import viewsets
from .models import (
    AboutUniversity, AboutCollege, Faculty, Lyceum, Student, Event, EventImage, Library,
    JobTitle, LanguageKnowledge, LaborActivity, Management, Structure, Recruitment,
    Document, Direction, DSC, Сontacts, OtherLinks, Followus
)
from .serializers import (
    AboutUniversitySerializer, AboutCollegeSerializer, FacultySerializer, LyceumSerializer,
    EventSerializer, EventImageSerializer, LibrarySerializer, JobTitleSerializer,
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


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentRegisterSerializer, VerifyCodeSerializer


class StudentRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            try:
                student = Student.objects.get(student_id=student_id)
                if student.is_verified:
                    return Response({'detail': 'Этот студент уже верифицирован.'}, status=status.HTTP_400_BAD_REQUEST)
                # Отправка кода подтверждения (реализуйте логику отправки, например, через SMS)
                return Response({'detail': 'Код подтверждения отправлен.'}, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({'detail': 'Ваш номер не найден в базе студентов.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyCodeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            verification_code = serializer.validated_data['verification_code']
            try:
                student = Student.objects.get(student_id=student_id)
                if student.verification_code == verification_code:
                    student.is_verified = True
                    student.save()
                    return Response({'detail': 'Вы успешно вошли в библиотеку.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Ошибка: неверный код подтверждения.'},
                                    status=status.HTTP_400_BAD_REQUEST)
            except Student.DoesNotExist:
                return Response({'detail': 'Ваш номер не найден в базе студентов.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import IsAuthenticated


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        student_id = self.request.user.student.student_id
        if Student.objects.filter(student_id=student_id, is_verified=True).exists():
            return super().get_queryset()
        else:
            return Library.objects.none()


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
