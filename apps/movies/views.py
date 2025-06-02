from django.shortcuts import render

def movies_view(request):
    return render(request, 'movies.html')

def single_movie_view(request):
    return render(request, 'single-movie.html')
