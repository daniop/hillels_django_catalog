from django.db import models
from django.utils.translation import gettext_lazy as _


class Commodity(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Retailer(models.Model):
    title = models.CharField(max_length=100)
    city = models.OneToOneField(City, verbose_name=_("city"), on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey("City", verbose_name=_("city"), on_delete=models.SET_NULL, null=True)
    commodity = models.ManyToManyField(Commodity, verbose_name=_("commodity"), blank=True)

    def __str__(self):
        return self.last_name
