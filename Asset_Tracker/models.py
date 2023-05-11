from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    domain = models.CharField(max_length=255, unique=True)
    employees = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    serial_number = models.CharField(max_length=255, unique=True)
    condition = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    devices = models.ManyToManyField(Device, through='Subscription')

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_date = models.DateTimeField(auto_now_add=True)
    checked_in_date = models.DateTimeField(null=True, blank=True)
    checked_out_condition = models.CharField(max_length=255, null=True, blank=True)
    checked_in_condition = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.device.name + ' - ' + self.subscriber.user.username
