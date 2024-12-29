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
   git clone https://github.com/your-repo/online-course-mgmt.git
   cd online-course-mgmt
