# Generated by Django 5.1.7 on 2025-03-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='current_location',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='dropoff_location',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trip',
            name='pickup_location',
            field=models.FloatField(max_length=255),
        ),
    ]
