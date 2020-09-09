from django.db import models
from django import forms


class MovieItem(models.Model):
    imdb_id = models.CharField(max_length=10, db_index=True)
    title = models.CharField(max_length=300)
    year = models.IntegerField(blank=True)
    poster = models.ImageField()
    type = models.CharField(blank=True, choices=[(kind, kind) for kind in ['movie', 'series', 'episode']], max_length=7)

    def __str__(self):
        return f'"{self.title}", {self.type} ({self.year})'


class SearchForm(forms.ModelForm):
    class Meta:
        model = MovieItem
        fields = ['title', 'year', 'type']
        labels = {'title': 'Title', 'year': 'Year', 'type': 'Type'}

