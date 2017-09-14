from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from . choices import *


# Create your models here.
class QuotationRequests(models.Model):
        first_name = models.CharField(max_length=155)
        last_name = models.CharField(max_length=155)
        email = models.EmailField()
        home_info = models.ManyToManyField("HouseInformation", related_name="home_infos")
        home_info_boost = models.CharField(max_length=155, default=None)
        service_type = MultiSelectField(choices=service_choices)
        extra_service = MultiSelectField(choices=extra_service_choices, default=None, null=True, blank=True)
        # extra_service = models.ManyToManyField("ExtraService", related_name="extra_service")
        # square_feet = models.ManyToManyField("SquareFeet", related_name="square_feet")
        square_feet = models.CharField(max_length=155, default=None)
        check_if_carpet = models.BooleanField(default=False,
            verbose_name="Check if you have carpet")
        rate_home = models.IntegerField(default = 10)
        # telephone = PhoneNumberField()
        telephone = models.CharField(max_length=10)
        address = models.CharField(max_length=300)
        apt_suite = models.CharField(max_length=100, null = True, blank = True)
        city = models.CharField(max_length=100)
        state = models.CharField(max_length=5)
        zip_code = models.CharField(max_length=5)
        booking_date = models.DateField(default=datetime.now)
        referrer = models.CharField(max_length=15, choices = referrer_choices)
        # booking_time = models.TimeField()

        def __str__(self):
            return f"{self.last_name}, {self.first_name}"

        # Edit to show info on quotation
        def list_quotations(self, *args, **kwargs):
            return ", ".join([quote.cleaning for quote in self.type_of_cleanings.all()])

# Create class for type of cleaning
class HouseInformation(models.Model):
    house = models.CharField(max_length=155)
    def __str__(self):
        return self.house

# Create class for service type
class ServiceType(models.Model):
    service = models.CharField(max_length=155)
    def __str__(self):
        return self.service

# Create class for extra service
class ExtraService(models.Model):
    extra = models.CharField(max_length=155)
    def __str__(self):
        return self.extra

# Create class for Square Feet
class SquareFeet(models.Model):
    square_footage = models.CharField(max_length=55)
    def __str__(self):
        return self.square_footage
