from django.db import models

from projects.models.common import Comment


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


class MapComment(Comment):
    project = 'Bot'
