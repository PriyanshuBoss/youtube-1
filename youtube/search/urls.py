from django.contrib import admin
from django.urls import path
from .views import SearchView, FetchView, SetApiKey

urlpatterns = [
    path('search', SearchView.as_view(), name="search_video_list"),
    path('fetch_data', FetchView.as_view(), name="fetch_data"),
    path('set_api_key', SetApiKey.as_view(), name="set_api_key")

]
