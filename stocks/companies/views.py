from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from . import app
import datetime
import math
import random
from companies.models import Company, Model, Predictions

class prediction_data:
    def __init__(self):
        self.name = ""
        self.ticker = ""
        self.prediction = 0
        self.yesterday = 0
        self.r_squared = 0
        self.percent_gain = 0

    def calc_gain(self):
        if self.yesterday != 0:
            self.percent_gain = (self.prediction - self.yesterday) / self.yesterday * 100




def index(request):
    return HttpResponse("Hello, Django!")

def set(request):
    data = app.get_companies()
    existing = Company.objects.all()
    names = []
    for existing_company in existing:
        names.append(existing_company.name)
    for item in data:
        if item[1] not in names:
            company = Company(name=item[1], ticker=item[0], industry=item[2])
            company.save()
    return HttpResponse("Success...?")

def get(request, company_id):
    company = Company.objects.get(id=company_id)
    app.writeFile(company.ticker)
    return HttpResponse(company.name + " Added")

def generate_sample_of_models(request):
    companies = Company.objects.all()
    for company in companies:
        try:
            test_rsquared = app.generate_model(company.ticker)
            print(test_rsquared)
            model = Model(company_id=company.id, test_rsquared=test_rsquared, date=datetime.date.today())
            model.save()
        except:
            print("unsuccessful")
    return HttpResponse("Potential Models Added")

def update_csv(request, company_id):
    company = Company.objects.get(id=company_id)
    print(company.ticker)
    app.update_csv(company.ticker)
    return HttpResponse("CSV Updated")

def clean(request, company_id):
    company = Company.objects.get(id=company_id)
    app.clean(company.ticker)
    return HttpResponse("CSV Updated")

def predict(request, company_id):
    company = Company.objects.get(id=company_id)
    prediction = app.use_regressor(company.ticker)
    print(prediction)
    return HttpResponse(prediction)

def actual(request, company_id, date):
    company = Company.objects.get(id=company_id)
    actual = app.actual(company.ticker, date)
    print(actual)
    return HttpResponse(actual)

def overnight(request):
    companies = Company.objects.all()
    for company in companies:
        try:
            app.clean(company.ticker)
        except:
            print("Cannot clean CSV file for ", company.ticker)
        try:
            app.update_csv(company.ticker)
        except:
            print("Cannot update CSV for ", company.ticker)
        try:
            actual = app.actual(company.ticker)
            yesterday_prediction = Predictions.objects.filter(company_id=company.id).order_by('date')[0]
            yesterday_prediction.actual = actual
            yesterday_prediction.accuracy = (actual - yesterday_prediction.prediction) / yesterday_prediction.yesterday
            yesterday_prediction.save()
        except:
            print("Cannot get actual data for ", company.ticker)
        try:
            app.update_regressor(company.ticker)
        except:
            print("Cannot update model for ", company.ticker)
        try:
            number = app.use_regressor(company.ticker)
            prediction = Predictions(company_id=company.id, prediction=number[0], yesterday=number[1], date=datetime.date.today())
            prediction.save()
        except:
            print("Unable to make prediction for ", company.ticker)
    return HttpResponse(True)

def add_models_to_database(request):
    companies = Company.objects.all()
    for company in companies:
        try:
            accuracy = app.get_model_accuracy(company)
            print(accuracy)
        except:
            print(company.ticker)
    return HttpResponse(True)

def show_predictions(request):
    output = []
    companies = Company.objects.all()
    for company in companies:
        data = prediction_data()
        data.name = company.name
        data.ticker = company.ticker
        try:
            model = Model.objects.get(company_id=company.id)
            data.r_squared = model.test_rsquared
        except:
            data.r_squared = 0
        try:
            prediction = Predictions.objects.get(company_id=company.id)
            data.prediction = prediction.prediction
            data.yesterday = prediction.yesterday
        except:
            data.prediction = 0
        data.calc_gain()
        output.append(data)
    output = sorted(output, key=lambda x: x.percent_gain)
    for company in output:
        print(company.name, company.ticker, company.percent_gain, company.prediction, company.yesterday, company.r_squared)
    return HttpResponse(output)
