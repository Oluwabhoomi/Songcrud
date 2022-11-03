from django.urls import path

from .views import SongList, SongDetail, ArtisteList, ArtisteDetail

urlpatterns = [
    path("<int:pk>/", SongDetail.as_view(), name="song_detail"),
    path("", SongList.as_view(), name="song_list"),
    path("<int:pk>/", ArtisteDetail.as_view(), name="artiste_detail"),
    path("", ArtisteList.as_view(), name="artiste_list"),
]
    