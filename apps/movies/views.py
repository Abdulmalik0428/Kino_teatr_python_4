from django.shortcuts import render
from .models import Movie



def movies_view(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', context={'movies':movies})

def single_movie_view(request):
    return render(request, 'single-movie.html')
