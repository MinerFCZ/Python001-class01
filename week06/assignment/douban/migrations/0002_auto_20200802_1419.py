# Generated by Django 2.2.13 on 2020-08-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douban', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_comment',
            name='comment_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie_comment',
            name='rating',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
