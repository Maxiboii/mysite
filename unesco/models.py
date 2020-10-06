from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name


class State(models.Model):
    name = models.CharField(null=True, max_length=128)

    def __str__(self) :
        return self.name


class Region(models.Model):
    name = models.CharField(null=True, max_length=128)

    def __str__(self) :
        return self.name


class Iso(models.Model):
    name = models.CharField(null=True, max_length=128)

    def __str__(self) :
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(null=True, max_length=1024)
    justification = models.CharField(null=True, max_length=512)
    year = models.IntegerField(null=True)
    longitude = models.DecimalField(null=True, max_digits=20, decimal_places=4)
    latitude = models.DecimalField(null=True, max_digits=20, decimal_places=4)
    area_hectares = models.DecimalField(null=True, max_digits=20, decimal_places=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE,null=True)

    def __str__(self) :
        return self.name