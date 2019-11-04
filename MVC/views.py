from django.shortcuts import render, HttpResponse
from django.views import generic 

from . models import Movie
# Create your views here.

def HelloWorld(request):
    return HttpResponse("My Movie List Hello from our View Template!")

class IndexView(generic.ListView):
    model = Movie
    template_name = 'movies_list.html'
    #context_object_name = 'movie_list'

class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'