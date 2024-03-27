from django.urls import path

from .views import IndexView, ReviewView

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("review/", ReviewView.as_view(), name="review"),
]
