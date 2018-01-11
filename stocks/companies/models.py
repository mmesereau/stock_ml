from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=200)
    industry = models.CharField(max_length=200)

class Model(models.Model):
    company_id = models.IntegerField(default=0)
    hidden_layer_sizes = models.IntegerField(default=0)
    activation = models.CharField(max_length=200)
    solver = models.CharField(max_length=200)
    train_rsquared = models.FloatField(default=0)
    test_rsquared = models.FloatField(default=0)
    date = models.DateTimeField('date created')

class Predictions(models.Model):
    company_id = models.IntegerField(default=0)
    date = models.DateTimeField('prediction for this date')
    prediction = models.FloatField(default=0)
