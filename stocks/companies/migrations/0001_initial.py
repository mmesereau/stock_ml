# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-10 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ticker', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(default=0)),
                ('hidden_layer_sizes', models.IntegerField(default=0)),
                ('activation', models.CharField(max_length=200)),
                ('solver', models.CharField(max_length=200)),
                ('train_rsquared', models.FloatField(default=0)),
                ('test_rsquared', models.FloatField(default=0)),
                ('date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField(default=0)),
                ('date', models.DateTimeField(verbose_name='prediction for this date')),
                ('prediction', models.FloatField(default=0)),
            ],
        ),
    ]
