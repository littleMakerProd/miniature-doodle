import cineplex

def scheduled_job():
    cineplex.get_movies_playing_now()
    print('This job is run every weekday at 5pm.')

