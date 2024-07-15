# Generated by Django 5.0.6 on 2024-07-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0002_remove_event_location_event_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]