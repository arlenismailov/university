# univer_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StudentViewSet, LibraryViewSet, AboutUniversityViews, AboutCollegeViews, FacultyViews, ProfessorViews

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'university', AboutUniversityViews)
router.register(r'college', AboutCollegeViews)
router.register(r'faculty', FacultyViews)
router.register(r'professors', ProfessorViews)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
