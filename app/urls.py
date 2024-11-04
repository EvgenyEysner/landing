from django.urls import path
from django.views.generic import TemplateView

from .views import IndexView, ReviewView

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("<int:team_id>/review/", ReviewView.as_view(), name="review"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]
