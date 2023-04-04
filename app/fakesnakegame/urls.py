from django.urls import path

from . import views

urlpatterns = [
    path("fakesnakegame", views.fakesnakegame, name="fakesnakegame"),
    path("downloadfakesnakegame/", views.download_file, name="downloadfakesnakegame"),
]
