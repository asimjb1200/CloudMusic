from django.contrib import admin
from .models import Album, Song

# Register models that should have an interface on the admin page
admin.site.register(Album)
admin.site.register(Song)

