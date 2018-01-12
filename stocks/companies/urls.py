from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('set/', views.set, name='set'),
    path('get/<int:company_id>/', views.get, name='get'),
    path('test_model/<int:company_id>/', views.generate_sample_of_models, name="sample"),
    path('update_csv/<int:company_id>/', views.update_csv, name="update_csv"),
    path('', views.index, name='index'),
]
