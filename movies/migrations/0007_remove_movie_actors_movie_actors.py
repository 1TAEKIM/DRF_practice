# Generated by Django 4.0 on 2024-06-03 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_actor_movies_movie_actors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movies.Actor'),
        ),
    ]
