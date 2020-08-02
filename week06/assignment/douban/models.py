from django.db import models


# Create your models here.

class movie_comment(models.Model):
    movie_id = models.CharField(max_length=100)
    user_name = models.CharField(max_length=150)
    rating = models.SmallIntegerField(null=True, blank=True)
    comment_time = models.DateTimeField(null=True, blank=True)
    short_content = models.CharField(max_length=800)
