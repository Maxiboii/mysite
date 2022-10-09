from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Population(models.Model):
    region = models.CharField(max_length=100)
    population = models.IntegerField()


class CasesToday(models.Model):
    region = models.ForeignKey('Population', on_delete=models.CASCADE, null=True)
    cases = models.IntegerField()
    indx = models.FloatField(null=True)
    color = models.FloatField(null=True)


class Map(models.Model):
    data = models.CharField(max_length=3000)
    cases = models.ForeignKey('CasesToday', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey('Population', on_delete=models.CASCADE, null=True)


class Utility(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=20)


class MapComment(models.Model) :
    text = models.TextField(
        validators=[MinLengthValidator(3, "Comment must be greater than 3 characters")]
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        if len(self.text) < 15 : return self.text
        return self.text[:11] + ' ...'
