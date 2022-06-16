from django.contrib import admin
from .models import Bb, Rubric

@admin.register(Bb)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'published','rubric']


admin.site.register(Rubric)
class BdAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'price', 'published', 'rubric']