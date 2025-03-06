from django.db import models







class Weather(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    temp_c = models.FloatField()
    temp_color = models.CharField(max_length=7)  # Hex rang kodi
    wind_kph = models.FloatField()
    wind_color = models.CharField(max_length=7)  # Hex rang kodi
    cloud = models.IntegerField()
    cloud_color = models.CharField(max_length=7)  # Hex rang kodi
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}, - {self.name}, - {self.country}, - {self.created_at.strftime('%Y-%m-%d    %H:%M')}"

