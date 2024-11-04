import csv
import re

from django.core.management.base import BaseCommand

from app.models import Rating


def extract_team_number(team_str):
    """Extracts the team number from the given team string."""
    match = re.search(r"\d+", team_str)
    return int(match.group()) if match else 1


def add_review(file_path):
    """Fügt Bewertungen aus einer CSV-Datei hinzu."""
    try:
        with open(file_path, encoding="UTF-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                team_number = extract_team_number(row["team"])

                Rating.objects.create(
                    star=int(row["star"]),
                    review=row["review"],
                    created=row["created"],
                    username=row["username"],
                    team_id=team_number,
                )
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


class Command(BaseCommand):
    help = "Fügt Bewertungen aus einer CSV-Datei hinzu."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Pfad zur CSV-Datei")

    def handle(self, *args, **options):
        file_path = options["file_path"]
        add_review(file_path)
