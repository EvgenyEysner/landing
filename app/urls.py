from django.urls import path
from django.views.generic import TemplateView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from .views import IndexView, ReviewView, Rating

info_dict = {
    "queryset": Rating.objects.all(),
    "date_field": "created",
}


urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("review/", ReviewView.as_view(), name="review"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"reviews": GenericSitemap(info_dict)}},
    ),
]
