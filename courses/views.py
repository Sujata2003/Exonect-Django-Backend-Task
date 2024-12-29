# Import necessary modules and classes
from django.shortcuts import render  # Import render function for rendering templates
from rest_framework.decorators import api_view  # Import api_view decorator for creating API views
from rest_framework.response import Response  # Import Response class for returning API responses
from rest_framework import viewsets  # Import viewsets for creating RESTful APIs
from .models import Course, Enrollment, Lesson, Category  # Import models
from .serializers import CourseSerializer, EnrollmentSerializer, LessonSerializer, CategorySerializer  # Import serializers
from django.core.cache import cache  # Import cache for caching data
from django.http import HttpResponse
# Function to retrieve cached courses or fetch from the database if not cached
def get_cached_courses():
    courses = cache.get('courses')  # Try to get courses from cache
    if not courses:  # If not found in cache
        courses = list(Course.objects.all())  # Fetch all courses from the database
        cache.set('courses', courses, timeout=300)  # Cache the courses for 5 minutes (300 seconds)
    return courses

# API view for getting cached courses
@api_view(['GET'])
def cached_courses(request):
    courses = get_cached_courses()  # Get cached or fresh courses
    serializer = CourseSerializer(courses, many=True)  # Serialize the course data
    return Response(serializer.data)  # Return the serialized data in the response

# ViewSet for handling CRUD operations for Course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()  # Queryset to retrieve all courses
    serializer_class = CourseSerializer  # Serializer class for course serialization

    # Override perform_create to invalidate cache after creating a course
    def perform_create(self, serializer):
        super().perform_create(serializer)  # Call the parent class's perform_create method
        cache.delete('courses')  # Invalidate the cached courses

    # Override perform_update to invalidate cache after updating a course
    def perform_update(self, serializer):
        super().perform_update(serializer)  # Call the parent class's perform_update method
        cache.delete('courses')  # Invalidate the cached courses

    # Override perform_destroy to invalidate cache after deleting a course
    def perform_destroy(self, instance):
        super().perform_destroy(instance)  # Call the parent class's perform_destroy method
        cache.delete('courses')  # Invalidate the cached courses

# ViewSet for handling CRUD operations for Enrollment
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()  # Queryset to retrieve all enrollments
    serializer_class = EnrollmentSerializer  # Serializer class for enrollment serialization

# ViewSet for handling CRUD operations for Lesson
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()  # Queryset to retrieve all lessons
    serializer_class = LessonSerializer  # Serializer class for lesson serialization

# ViewSet for handling CRUD operations for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Queryset to retrieve all categories
    serializer_class = CategorySerializer  # Serializer class for category serialization

def home(request):
    return HttpResponse('<h1>Welcome to the Online Course Management System..<h1>')