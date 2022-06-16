from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="board/")),
    path('board/', include('bboard.urls', namespace='board')),
]
