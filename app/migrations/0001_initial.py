# Generated by Django 5.1.5 on 2025-01-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('temp_c', models.FloatField()),
                ('temp_color', models.CharField(max_length=7)),
                ('wind_kph', models.FloatField()),
                ('wind_color', models.CharField(max_length=7)),
                ('cloud', models.IntegerField()),
                ('cloud_color', models.CharField(max_length=7)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
