# Generated by Django 2.2.13 on 2020-08-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=150)),
                ('short_content', models.CharField(max_length=800)),
            ],
        ),
    ]