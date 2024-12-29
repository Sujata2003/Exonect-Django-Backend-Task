# Online Course Management System

This project is a comprehensive **Online Course Management System** built using Django and Django REST Framework. It allows users to manage courses, categories, lessons, and enrollments. The system includes API endpoints, caching with Redis, background task handling with Celery, and JWT-based authentication.

---

## Features
- **Course Management**: Create, read, update, and delete courses with associated categories and lessons.
- **User Enrollments**: Manage course enrollments for users.
- **Caching**: Optimize API responses using Redis caching.
- **Background Tasks**: Send welcome emails to users using Celery.
- **Authentication**: Secure APIs with JWT authentication.

---

## Project Setup 

### Prerequisites
- Python 3.9+
- PostgreSQL
- Redis
- Virtualenv (optional but recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Exonect-Django-Backend-Task/online-course-mgmt.git
   cd online-course-mgmt
   ```
--
### Project Setup steps:
1. Create and Activate a Virtual Environment
    ```bash
   python -m venv venv  
   venv\Scripts\activate
    ```

2. Install Dependencies
  ```bash
   pip install -r requirements.txt
  ```
3. Configure the Database
- Update the DATABASES settings in settings.py with your PostgreSQL credentials.
   ```bash
      DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',  # Specify the database engine as PostgreSQL
           'NAME': 'your_db',  # Name of the database
           'USER': 'youruser',  # Database user
           'PASSWORD': 'password',  # Password for the database user
           'HOST': 'localhost',  # Host where the database server is running
           'PORT': '5432',  # Port on which the database server is listening (default for PostgreSQL)
       }
   }
  ```
4. Run Migrations
  ```bash
   python manage.py makemigrations
   python manage.py migrate
  ```

5. Start the Development Server
   ```bash
   python manage.py runserver
   
   ```
---
## API Documentation
### Postman Collection
- Download the Postman Collection to explore available APIs for managing courses, lessons, enrollments, and categories.

### Endpoints
- **Course**: /api/courses/ 
- **Enrollments**: /api/enrollments/ 
- **Lessons**:  /api/lessons/ 
- **Categories**:  /api/categories/ 
- **Cached Courses**:  /api/courses/cached/ 
---
## Running Background Tasks with Celery
   - Start the Celery Worker
   ```bash
   celery -A online_course worker --loglevel=info
   ```

## Sending Welcome Emails
   - To test the welcome email functionality:
     - 1. Ensure the email backend is properly configured in settings.py.
     - 2. Trigger the task by calling the send_welcome_email function with a valid email address
      
      ```bash
      from courses.tasks import send_welcome_email
      send_welcome_email.delay('user@example.com')
      
      ```

## Caching with Redis

   - The cached_courses endpoint retrieves cached course data.
   - Data is cached for 5 minutes to improve performance.
   - The cache is automatically invalidated when a course is created, updated, or deleted.
