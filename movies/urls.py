from django.urls import path
from .views import *

urlpatterns = [
    # path('movies', movie_list),
    path('movies/', MovieList.as_view()),
    # path('movies/<int:pk>', movie_detail),
    path('movies/<int:pk>', MovieDetail.as_view()),
    # path('actors/', actor_list),
    path('actors/', ActorList.as_view()),
    # path('actors/<int:pk>', actor_detail),
    path('actors/<int:pk>', ActorDetail.as_view()),
    path('movies/<int:pk>/reviews', review_list)
]
