from django.contrib import admin
from django.utils.html import format_html

from .models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ["name", "phone", "email", "text", "created"]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="width: 1339px; height: 729px;"/>'.format(
                obj.image.url
            )
        )

    image_tag.short_description = "bild"
    list_display = ["image_tag", "name"]


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="width: 754px; height: 524px;"/>'.format(obj.image.url)
        )

    image_tag.short_description = "bild"
    list_display = ["image_tag", "name"]


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="width: 290px; height: 284px;"/>'.format(
                obj.avatar.url
            )
        )

    image_tag.short_description = "avatar"
    list_display = ["image_tag", "job"]


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="width: 27px; height: 27px;"/>'.format(obj.icon.url)
        )

    list_display = ["name", "image_tag", "link"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["team", "star", "username", "address", "review"]


@admin.register(InstallationTeam)
class InstallationTeamAdmin(admin.ModelAdmin):
    list_display = ["team_number"]
