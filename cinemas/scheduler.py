from apscheduler.schedulers.blocking import BlockingScheduler
import cineplex

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=0, minute=46)
def scheduled_job():
    get_movies_playing_now()
    print('This job is run every weekday at 5pm.')

sched.start()
