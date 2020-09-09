from django.shortcuts import render, reverse
from django.views.generic import TemplateView

from .models import SearchForm
from .services import get_movie_items


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
