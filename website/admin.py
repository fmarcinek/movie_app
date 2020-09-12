from django.contrib import admin
from .models import Favorites, MovieItem

# Register your models here.
admin.site.register(Favorites)
admin.site.register(MovieItem)

