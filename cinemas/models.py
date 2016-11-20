from django.db import models

# Create your models here.

class Cinema(models.Model):
    cinema_name = models.CharField(max_length=200)
    cinema_address = models.CharField(max_length=200)

    def __str__(self):
        return self.cinema_name


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=200)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_title

class Screening(models.Model):
    time = models.DateTimeField(auto_now=False, auto_now_add=False) 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.time)

