from django.shortcuts import render
from .models import movie_comment


# Create your views here.
def movie_comment_page(request):
    result = movie_comment.objects.filter(rating__gt=3)
    return render(request, 'result.html', locals())
