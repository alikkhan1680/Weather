import django
import os

# Django loyihasini ishga tushirish uchun settings.py ni ulaymiz
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from app import save_weather_for_all_countries

save_weather_for_all_countries()
