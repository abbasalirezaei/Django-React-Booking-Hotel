# Generated by Django 4.2.5 on 2025-07-09 14:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_room_occupancy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='rating',
        ),
        migrations.AlterField(
            model_name='room',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
