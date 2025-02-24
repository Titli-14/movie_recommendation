from django.urls import path
from .views import get_movies, add_movie, search_movies, recommend_movies, add_review

urlpatterns = [
    path('movies/', get_movies, name='get_movies'),
    path('movies/add/', add_movie, name='add_movie'),
    path('movies/search/', search_movies, name='search_movies'),
    path('movies/recommend/', recommend_movies, name='recommend_movies'),
    path('reviews/add/', add_review, name='add_review'),
]