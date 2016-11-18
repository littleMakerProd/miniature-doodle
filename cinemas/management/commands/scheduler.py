from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand, CommandError
import cinemas.cineplex

sched = BlockingScheduler()

class Command(BaseCommand):
    
    @sched.scheduled_job('cron', day_of_week='mon-sun', hour=2, minute=26)
    def scheduled_job():
        cinemas.cineplex.get_movies_playing_now()
        print('This job is run every weekday at 5pm.')

    def handle(self, *args, **options):
        sched.start()


