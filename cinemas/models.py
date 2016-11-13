from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_description = models.CharField(max_length=20200)

    def __str__(self):
        return self.movie_title

