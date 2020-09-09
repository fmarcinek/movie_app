from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import SearchForm, MovieItem
from .services import get_movie_items, get_certain_movie_info


class MovieItemListView(TemplateView):
    template_name = 'website/movieitem_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'movie_items': get_movie_items(self.request)
        }
        return context


def home(request):
    form = SearchForm()
    return render(request, 'website/home.html', {'form': form, 'page': '1'})


class MovieDetailView(DetailView):
    model = MovieItem

    def get_object(self):
        imdb_id = self.kwargs.get('imdb_id')
        context = {
            'movie': get_certain_movie_info(imdb_id)
        }
        return context
