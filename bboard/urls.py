
from django.contrib import admin
from django.urls import path, include
from .views import BoardView, By_rubric, BbCreateView


app_name = 'board'

urlpatterns = [
    path('', BoardView.as_view(), name='index'),
    path('<int:rubric_id>/', By_rubric.as_view(), name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add' ),
    path('basic/', BbCreateView.as_view(), name='basic' ),

]
