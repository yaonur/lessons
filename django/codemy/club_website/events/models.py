from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=60)
    address = models.CharField(max_length=260)
    zip_code = models.CharField('Zip Code', max_length=60, blank=True)
    phone = models.CharField('Contact Phone', max_length=30, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Adress', blank=True)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField("Event Name", max_length=60)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(MyClubUser, blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
