from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    AboutUniversityViewSet, AboutCollegeViewSet, LyceumViewSet, FacultyViewSet, ProfessorViewSet, StudentViewSet,
    EventViewSet, LibraryViewSet, JobTitleViewSet, LanguageKnowledgeViewSet,
    LaborActivityViewSet, ManagementViewSet, StructureViewSet, RecruitmentViewSet, DocumentViewSet,
    DirectionViewSet, DocumentationViewSet, DSCViewSet, СontactsViewSetr, OtherLinksViewSet, FollowusViewSet,
    LinkViewSet, NewsViewSet, CheckStudentNumber
)


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 3 зоведения
    path('university/', AboutUniversityViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='university_list'),
    path('university/<int:pk>/',
         AboutUniversityViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='university_detail'),

    path('college/', AboutCollegeViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='college list'),
    path('college/<int:pk>/',
         AboutCollegeViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='college detail'),

    path('lyceum/', LyceumViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='lyceum list'),
    path('lyceum/<int:pk>/',
         LyceumViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='lyceum detail'),
    # users
    path('faculty/', FacultyViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='faculty_list'),
    path('faculty/<int:pk>/',
         FacultyViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='faculty detail'),

    path('professor/', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='professor list'),
    path('professor/<int:pk>/',
         ProfessorViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='professor detail'),

    path('student/', StudentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='student list'),
    path('student/<int:pk>/',
         StudentViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='student detail'),
    path('check_student_number/', CheckStudentNumber.as_view(), name='check_student_number'),

    # evets
    path('event/', EventViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='event list'),
    path('event/<int:pk>/',
         EventViewSet.as_view({'get': 'retrieve', 'pot': 'update', 'delete': 'destroy'}),
         name='event detail'),
    # библиотека
    path('library/', LibraryViewSet.as_view({'get': 'list'}),
         name='library list'),
    # Руководство
    path('management/', ManagementViewSet.as_view({'get': 'list'}),
         name='management list'),
    #  Структура
    path('structure/', StructureViewSet.as_view({'get': 'list'}),
         name='structure list'),
    #  Направление
    path('direction/', DirectionViewSet.as_view({'get': 'list'}),
         name='Direction list'),
    #  О колледже
    path('dsc/', DSCViewSet.as_view({'get': 'list'}),
         name='dsc list'),
    #  контакты
    path('сontacts/', СontactsViewSetr.as_view({'get': 'list'}),
         name='сontacts list'),
    path('otherLinks/', OtherLinksViewSet.as_view({'get': 'list'}),
         name='OtherLinks list'),
    path('followus/', FollowusViewSet.as_view({'get': 'list'}),
         name='followus list'),
    path('link/', LinkViewSet.as_view({'get': 'list'}),
         name='OtherLinks list'),
    path('news/', NewsViewSet.as_view({'get': 'list'}),
         name='news list'),

]
