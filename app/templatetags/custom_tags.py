from django import template
from ..models import Social, Team, Slider, Carousel


register = template.Library()


@register.simple_tag()
def get_social_links():
    """
    Display of social links networks
    """
    return Social.objects.all()


@register.simple_tag()
def get_team():
    """
    Display Employees
    """
    return Team.objects.all()


@register.simple_tag()
def get_slider_images():
    """
    Display Employees
    """
    return Slider.objects.all()


@register.simple_tag()
def get_carousel_images():
    """
    Display Employees
    """
    return Carousel.objects.all()