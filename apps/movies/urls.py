from django.urls import path
from apps.movies.views import movies_view , single_movie_view


urlpatterns = [
    path('', movies_view, name='movies'),  # bu /movies/ uchun ishlaydi
    path('single_movie', single_movie_view ,name = 'single_movie')
]

