from django.db import models
from django.core.validators import RegexValidator

class Restaurants(models.Model):
    title = models.CharField(max_length=100)
    jop_time = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restaurants/')
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Restaurant_info(models.Model):
    jop_time = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    info = models.TextField()
    tel = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^\+?[0-9\s\-\(\)]{9,20}$',
            message="Enter a valid phone number. Allowed formats: +1234567890, +1 234 567 890, etc."
        )]
    )

    def __str__(self):
        return self.address


class Menu(models.Model):
    image = models.ImageField(upload_to='restaurants/menus/')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title