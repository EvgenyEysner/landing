# Generated by Django 4.1.6 on 2024-04-22 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_alter_rating_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="team",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="team",
            name="last_name",
        ),
    ]