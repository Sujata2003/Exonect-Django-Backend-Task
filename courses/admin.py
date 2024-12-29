# Import necessary modules and classes
from django.contrib import admin
from .models import Course, Enrollment, Lesson, Category

# Register the Course model with custom admin configuration
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the Course admin panel
    list_display = ('title', 'instructor')
    
    # Fields that can be searched in the Course admin panel
    search_fields = ('title',)
    
    # Filters to apply in the Course admin panel based on categories
    list_filter = ('categories',)

# Register the Enrollment, Lesson, and Category models with the admin site
admin.site.register(Enrollment)  # Default registration, no custom configuration
admin.site.register(Lesson)       # Default registration, no custom configuration
admin.site.register(Category)      # Default registration, no custom configuration
