from celery import shared_task
from .models import User

@shared_task
def send_email_task(user_id):
    user = User.objects.get(id=user_id)
    # Simulate sending email logic
    print(f"Email sent to {user.email}")

@shared_task
def handle_file_upload(file_path):
    with open(file_path, 'r') as file:
        # Simulate processing logic
        pass
