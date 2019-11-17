from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

from .lesson_status import update_lesson_status

# define tasks here
def print_schedule_info():
    print("------------------------------------")
    print("30 seconds passed - Scheduler ran")
    print(datetime.now())
    print("------------------------------------")


#schedule the above tasks here
def main_schedule_controller():
    scheduler = BackgroundScheduler()
    scheduler.add_job(print_schedule_info, 'interval', minutes=0.5)
    scheduler.add_job(update_lesson_status, 'interval', minutes=0.5)
    scheduler.start()



