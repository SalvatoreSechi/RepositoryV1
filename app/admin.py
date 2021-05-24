from django.contrib import admin

# Register your models here.

from .models import Post

admin.site.register(Post)

from .models import Utente

admin.site.register(Utente)
