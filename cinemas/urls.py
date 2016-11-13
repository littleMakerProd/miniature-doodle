from django.conf.urls import url

from . import views

app_name =  'cinemas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/$', views.get_movies_today)
]
