from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField

SEX_PERSON = {
        "m": "male",
        "f": "female",
    }

class Person(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[
            MaxValueValidator(120),
            MinValueValidator(0)
        ])
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Для визуалиции объекта в shell 
    def __str__(self):
        return f" {self.first_name} {self.last_name}"


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    stars = models.FloatField(validators=[
            MinValueValidator(0.0), MaxValueValidator(5.0)
        ])
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name} {self.city}"