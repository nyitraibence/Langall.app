from app_teachers.models import Lesson
from datetime import datetime
import pytz

def update_lesson_status():
    lessons = Lesson.objects.filter(is_over=False)
    current_datetime = pytz.UTC.localize(datetime.now())

    print('Checking for outdated lessons')
    for lesson in lessons:
        if(lesson.end_time < current_datetime):
            print('Passed lesson found, with id: ', lesson.id)
            lesson.is_over = True
            lesson.save()