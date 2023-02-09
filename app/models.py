from django.core.validators import RegexValidator
from django.db import models


class Contact(models.Model):
    """
    Create customer request
    """
    name = models.CharField('Name', max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    phone = models.CharField(validators=[phone_regex], max_length=16, blank=True)  # Validator soll eine Liste sein
    email = models.EmailField('email', max_length=254)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'anfrage'
        verbose_name_plural = 'anfragen'
        ordering = ['-created']

    def __str__(self):
        return f'Name: {self.name}'


class Social(models.Model):
    """ Social accounts"""
    icon = models.FileField('icon', upload_to='icons/', help_text='maximale Bildgröße 27x27')
    name = models.CharField('social netzwerk', max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name = 'social account'
        verbose_name_plural = 'social accounts'

    def __str__(self):
        return self.name


class Team(models.Model):
    """
    Team
    """
    avatar = models.ImageField('foto', upload_to='images/team', help_text='maximale Bildgröße 290x284')
    first_name = models.CharField('vorname', max_length=200)
    last_name = models.CharField('nachname', max_length=200)
    job = models.CharField('beruf', max_length=64)

    class Meta:
        verbose_name = 'mitarbeiter'
        verbose_name_plural = 'mitarbeiter'


class Slider(models.Model):
    """
    Slider
    """
    name = models.CharField('projektname', max_length=32, help_text='maximal 32 Zeichen')
    image = models.ImageField('bild', upload_to='images/slider', help_text='maximale Bildauflösung 1339x729')
    location = models.CharField('ort eintragen', max_length=64, help_text='maximale Länge 64 Zeichen')
    price = models.CharField('preis eintragen', max_length=10, help_text='maximale Länge 10 Zeichen')
    square = models.CharField('qm eingeben', max_length=5, help_text='maximale Länge 5 Zeichen')

    class Meta:
        verbose_name = 'slider'

    def __str__(self):
        return self.name


class Carousel(models.Model):
    name = models.CharField('projektname', max_length=32, help_text='maximal 32 Zeichen')
    image = models.ImageField('bild klein', upload_to='images/carousel', help_text='maximale Bildauflösung 775x524')
    big_image = models.ImageField('bild groß', upload_to='images/carousel', help_text='maximale Bildauflösung 1200x800')
    status = models.CharField('bauphase', max_length=64, help_text='maximal 64 Zeichen')
    location = models.CharField('ort eintragen', max_length=64, help_text='maximal 64 Zeichnen')
    description = models.TextField('projektbeschreibung', max_length=500, help_text='maximal 500 Zeichnen')

    def __str__(self):
        return self.name

