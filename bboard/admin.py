from django.contrib import admin
from .models import Bb

@admin.register(Bb)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'published']