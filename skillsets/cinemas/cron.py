from cinemas.models import Movie
from django.utils import timezone

def my_scheduled_job():
    m = Movie(movie_title="movie " + str(timezone.now()))
    m.save()


