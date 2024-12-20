# Generated by Django 4.1.6 on 2024-03-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_carousel_big_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slider",
            name="location",
            field=models.CharField(
                blank=True,
                help_text="maximale Länge 64 Zeichen",
                max_length=64,
                null=True,
                verbose_name="ort eintragen",
            ),
        ),
        migrations.AlterField(
            model_name="slider",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="maximal 32 Zeichen",
                max_length=32,
                null=True,
                verbose_name="projektname",
            ),
        ),
        migrations.AlterField(
            model_name="slider",
            name="price",
            field=models.CharField(
                blank=True,
                help_text="maximale Länge 10 Zeichen",
                max_length=10,
                null=True,
                verbose_name="preis eintragen",
            ),
        ),
        migrations.AlterField(
            model_name="slider",
            name="square",
            field=models.CharField(
                blank=True,
                help_text="maximale Länge 5 Zeichen",
                max_length=5,
                null=True,
                verbose_name="qm eingeben",
            ),
        ),
    ]
