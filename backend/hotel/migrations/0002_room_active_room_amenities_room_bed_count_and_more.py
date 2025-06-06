# Generated by Django 4.2.5 on 2025-05-20 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='room',
            name='amenities',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AddField(
            model_name='room',
            name='bed_count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='room',
            name='bed_type',
            field=models.CharField(choices=[('single', 'تک نفره'), ('double', 'دو نفره'), ('king', 'کینگ'), ('twin', 'دوتخته جدا')], default='single', max_length=10),
        ),
        migrations.AddField(
            model_name='room',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2025-05-20 12:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='floor',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='room',
            name='guests_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='room',
            name='rating',
            field=models.FloatField(default=4.5),
        ),
        migrations.AddField(
            model_name='room',
            name='room_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='short_description',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='room',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
