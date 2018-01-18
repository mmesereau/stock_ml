from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)

class Model(models.Model):
    company_id = models.IntegerField(default=0)
    test_rsquared = models.FloatField(default=0)
    date = models.CharField(max_length=200)

class Predictions(models.Model):
    company_id = models.IntegerField(default=0)
    date = models.CharField(max_length=200)
    prediction = models.FloatField(default=0)
    actual = models.FloatField(default=0)
    yesterday = models.FloatField(default=0)
    accuracy = models.FloatField(default=0)
