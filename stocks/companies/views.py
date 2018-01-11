from django.shortcuts import render
from django.http import HttpResponse
from . import app
from companies.models import Company, Model, Predictions

def index(request):
    return HttpResponse("Hello, Django!")

def set(request):
    print("hit endpoint")
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
    print("hit endpoint")
    company = Company.objects.get(id=company_id)
    app.writeFile(company.ticker)
    return HttpResponse(company.name + " Added")
