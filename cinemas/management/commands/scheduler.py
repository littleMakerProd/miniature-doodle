from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand, CommandError
import cinemas.cineplex

sched = BlockingScheduler()

class Command(BaseCommand):
    
    @sched.scheduled_job('cron', day_of_week='mon-sun', hour=19, minute=31)
    def scheduled_job():
        cinemas.cineplex.find_showtime_in_jakarta_cinemas()
        print('This job is run every day at 6:12pm.')

    def handle(self, *args, **options):
        sched.start()


