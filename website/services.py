import requests
from movie_app.settings import OMDB_API_KEY, OMDB_API_URL


def get_movie_items(request):
    params = {
        'apikey': OMDB_API_KEY,
        's': request.GET['title'],
        'y': request.GET.get('year', ''),
        'type': request.GET.get('type', ''),
        'p': request.GET.get('page', '1'),
    }
    resp = requests.get(OMDB_API_URL, params=params)
    movie_items = resp.json()
    return movie_items['Search']
