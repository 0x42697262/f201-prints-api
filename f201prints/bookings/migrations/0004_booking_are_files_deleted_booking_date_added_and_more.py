# Generated by Django 4.2.5 on 2023-09-23 18:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_amount_to_pay_booking_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='are_files_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 23, 18, 45, 22, 908031, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_soft_deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='expected_delivery_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]