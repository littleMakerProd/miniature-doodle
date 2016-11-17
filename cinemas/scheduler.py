from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
@sched.scheduled_job('cron', day_of_week='mon-sun', hour=0, minute=32)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
