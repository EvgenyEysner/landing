from django.urls import path
from .views import IndexView
from django.views.decorators.cache import cache_page  # add cache

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
]
