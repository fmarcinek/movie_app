from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models import Exists

from .models import SearchForm, MovieItem, MovieItemForm, Favorites
from .services import get_movie_items, get_certain_movie_info


class MovieItemListView(LoginRequiredMixin, TemplateView):
    template_name = 'website/movieitem_list.html'

    def get_context_data(self, **kwargs):
        context = {
            'movie_items': get_movie_items(self.request)
        }
        return context


def home(request):
    form = SearchForm()
    return render(request, 'website/home.html', {'form': form, 'page': '1'})


def about(request):
    return render(request, 'website/about.html')


class MovieDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = MovieItem
    form_class = MovieItemForm

    def get_initial(self):
        movie_obj = self.get_object()['movie']
        initial_values = {
            'title': movie_obj['Title'],
            'year': movie_obj['Year'],
            'poster': movie_obj['Poster'],
            'imdb_id': movie_obj['imdbID'],
            'type': movie_obj['Type']
        }
        return initial_values

    def get_object(self):
        imdb_id = self.kwargs.get('imdb_id')
        context = {
            'movie': get_certain_movie_info(imdb_id)
        }
        return context


@login_required
def save_favorite(request, **kwargs):
    user = request.user
    movieitem_form = MovieItemForm(request.POST)
    movie_id = movieitem_form['imdb_id'].value()

    movie_items = MovieItem.objects.filter(imdb_id=movie_id)
    if not movie_items and movieitem_form.is_valid():
        movieitem_form.save()

    movie_item = MovieItem.objects.filter(imdb_id=movie_id).first()
    if not Favorites.objects.filter(user_id=user, movie_id=movie_item):
        favorite = Favorites(user_id=user, movie_id=movie_item)
        favorite.save()
        messages.success(request, f'This movie was successfully added to your favorites!')
    else:
        messages.warning(request, f'You already have this movie in your favorites')

    return redirect(reverse('website-movie', kwargs=kwargs))


class FavoritesListView(LoginRequiredMixin, ListView):
    model = MovieItem
    context_object_name = 'favorites'
    template_name = 'website/favorites_list.html'

    def get_queryset(self):
        return Favorites.objects.select_related('movie_id').filter(user_id=self.request.user).values(
            imdb_id=F('movie_id__imdb_id'),
            title=F('movie_id__title'),
            poster=F('movie_id__poster'),
            type=F('movie_id__type'),
            year=F('movie_id__year')
        )



