import redis
from .models import Course

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_cached_courses():
    courses = cache.get('courses')
    if not courses:
        courses = list(Course.objects.all().values())
        cache.set('courses', courses, ex=300)
    return courses
