from django.shortcuts import render
from django.http import HttpResponse
from . import app
import datetime
import math
import random
from companies.models import Company, Model, Predictions

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
    print("here")
    company = Company.objects.get(id=company_id)
    app.writeFile(company.ticker)
    return HttpResponse(company.name + " Added")

def generate_sample_of_models(request, company_id):
    company = Company.objects.get(id=company_id)
    for attempt in range(100):
        #randomize some parameters to identify effectiveness
        hidden_layer_sizes = math.ceil(random.random() * 10)
        activation = random.choice(["identity", "logistic", "tanh", "relu"])
        solver = random.choice(["lbfgs", "sgd", "adam"])
        max_iter = 10000
        r_squared = app.generate_model(company.ticker, hidden_layer_sizes, activation, solver, max_iter)
        results = Model(company_id=company_id, hidden_layer_sizes = hidden_layer_sizes, activation=activation,
                        solver=solver, train_rsquared = r_squared[0], test_rsquared = r_squared[1], date = datetime.date.today())

        results.save()
    return HttpResponse("Potential Models Added")
