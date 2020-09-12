from django.db import models
from django import forms
from django.contrib.auth.models import User


class MovieItem(models.Model):
    imdb_id = models.CharField(max_length=10, db_index=True)
    title = models.CharField(max_length=300)
    year = models.IntegerField(blank=True)
    poster = models.URLField(max_length=200)
    type = models.CharField(blank=True, choices=[(kind, kind) for kind in ['movie', 'series', 'episode']], max_length=7)

    def __str__(self):
        return f'"{self.title}", {self.type} ({self.year})'


class MovieItemForm(forms.ModelForm):
    class Meta:
        model = MovieItem
        fields = ['imdb_id', 'title', 'year', 'poster', 'type']


class SearchForm(forms.ModelForm):
    class Meta:
        model = MovieItem
        fields = ['title', 'year', 'type']
        labels = {'title': 'Title', 'year': 'Year', 'type': 'Type'}


class Favorites(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(MovieItem, on_delete=models.CASCADE)
