# Generated by Django 4.2.13 on 2024-06-20 20:43

import booking_service.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_service', '0010_alter_hotel_photo_alter_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='info',
            field=models.FileField(blank=True, null=True, upload_to='profile_info/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['doc']), booking_service.validators.validate_doc_extension]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users_photo/', verbose_name='User photo'),
        ),
    ]
