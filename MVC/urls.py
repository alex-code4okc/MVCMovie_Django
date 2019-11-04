from django.urls import path, include

from . import views
from . import models

app_name = 'mvc'
urlpatterns = [
    
    path('',views.HelloWorld,name='HelloWorld'),
    path('index',views.HelloWorld,name='HelloWorldIndex'),
    path('movies',views.IndexView.as_view(),name='MoviesIndex'), # list all movies
    path('movies/details/<int:pk>',views.DetailView.as_view(),name='MovieDetail'),
    #path('movies/edit/<int:pk>',views.edit,name='edit'),
]