# Generated by Django 4.2.13 on 2024-05-31 22:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0007_alter_booking_check_in_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(18)]),
        ),
    ]
