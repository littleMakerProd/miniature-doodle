from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand, CommandError
import cinemas.cineplex

sched = BlockingScheduler()

class Command(BaseCommand):
    
    @sched.scheduled_job('cron', day_of_week='mon-sun', hour=7, minute=00)
    def scheduled_job():
        cinemas.cineplex.find_showtime_in_jakarta_cinemas()
        print('FindShowTimeInJakarta is run every day at 7:00am.')

    def handle(self, *args, **options):
        sched.start()


