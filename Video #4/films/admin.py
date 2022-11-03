from django.contrib import admin
from . models import User
from . models import Film, Song

admin.site.register(User)
admin.site.register(Film)
admin.site.register(Song)