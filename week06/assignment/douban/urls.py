from django.urls import path
from . import views

urlpatterns = [
    path('comment', views.movie_comment_page)

]