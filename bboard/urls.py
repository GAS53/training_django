
from django.contrib import admin
from django.urls import path, include
from .views import BoardView 


app_name = 'board'

urlpatterns = [
    path('', BoardView.as_view() ),
    
    
]
