from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('set/', views.set, name='set'),
    path('<int:company_id>/', views.get, name='get'),
    path('', views.index, name='index'),
]
