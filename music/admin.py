from django.contrib import admin

from .models import Song
from .models import Album
from .models import Artist


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)