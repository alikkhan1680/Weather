from django.core.management.base import BaseCommand
from app.wetherServis import save_weather_for_all_countries

class Command(BaseCommand):
    help = 'Fetch and save weather data for all countries'

    def handle(self, *args, **kwargs):
        self.stdout.write("Fetching weather data ...\n")
        save_weather_for_all_countries()
        self.stdout.write(self.style.SUCCESS("successfully fetched and save weather data"))