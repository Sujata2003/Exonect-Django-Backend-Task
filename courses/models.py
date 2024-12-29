# Import necessary modules and classes
from django.db import models
from django.contrib.auth.models import User

# Define the Category model to represent course categories
class Category(models.Model):
    # Name field with a maximum length of 100 characters
    name = models.CharField(max_length=100)

# Define the Course model to represent courses offered in the system
class Course(models.Model):
    # Title of the course with a maximum length of 200 characters, indexed for faster queries
    title = models.CharField(max_length=200, db_index=True)
    
    # Description of the course as a text field
    description = models.TextField()
    
    # Foreign key relationship with the User model to associate an instructor with the course
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Many-to-many relationship with Category, allowing multiple categories per course
    categories = models.ManyToManyField(Category, related_name="courses")

# Define the Enrollment model to track user enrollments in courses
class Enrollment(models.Model):
    # Foreign key relationship with User to link the enrollment to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Foreign key relationship with Course to link the enrollment to a specific course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    # Timestamp for when the user enrolled, automatically set on creation
    enrolled_at = models.DateTimeField(auto_now_add=True)

# Define the Lesson model to represent lessons associated with a course
class Lesson(models.Model):
    # Foreign key relationship with Course, linking lessons to a specific course
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    
    # Title of the lesson with a maximum length of 200 characters
    title = models.CharField(max_length=200)
    
    # Content of the lesson as a text field
    content = models.TextField()
