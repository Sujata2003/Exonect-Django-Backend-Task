# Import necessary modules from the Django REST Framework
from rest_framework import serializers
from .models import Course, Enrollment, Lesson, Category

# Serializer for the Lesson model
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson  # Specify the model associated with this serializer
        fields = '__all__'  # Include all fields from the Lesson model

# Serializer for the Course model
class CourseSerializer(serializers.ModelSerializer):
    # Nesting the LessonSerializer to include lessons in the Course representation
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course  # Specify the model associated with this serializer
        fields = '__all__'  # Include all fields from the Course model

# Serializer for the Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment  # Specify the model associated with this serializer
        fields = '__all__'  # Include all fields from the Enrollment model

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Specify the model associated with this serializer
        fields = '__all__'  # Include all fields from the Category model
