from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, EnrollmentViewSet, LessonViewSet,CategoryViewSet,home

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')  # Specify basename
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')  # Specify basename
router.register(r'lessons', LessonViewSet)          # Endpoint for lesson operations
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('',home,name='home'),

]
