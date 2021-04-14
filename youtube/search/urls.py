from django.contrib import admin
from django.urls import path
from .views import search, fetch_data

urlpatterns = [
    path('search', search, name="search_video_list"),
    path('fetch_data', fetch_data, name="fetch_data"),

]
