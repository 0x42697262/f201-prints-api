# Generated by Django 4.2.5 on 2023-09-23 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_are_files_deleted_booking_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]