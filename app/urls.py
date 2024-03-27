from django.urls import path
from .views import IndexView, ReviewView, ContactView
from django.views.decorators.cache import cache_page  # add cache

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("review/", ReviewView.as_view(), name="review"),
    # path('rate/', rate_image, name='rate-view'),
]
