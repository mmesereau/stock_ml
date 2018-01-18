from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('set/', views.set, name='set'),
    path('get/<int:company_id>/', views.get, name='get'),
    path('test_model/', views.generate_sample_of_models, name="sample"),
    path('update_csv/<int:company_id>/', views.update_csv, name="update_csv"),
    path('clean/<int:company_id>/', views.clean, name="clean"),
    path('predict/<int:company_id>/', views.predict, name="predict"),
    path('actual/<int:company_id>/<str:date>/', views.actual, name="actual"),
    path('overnight/', views.overnight, name="overnight"),
    path('add_models_to_database/', views.add_models_to_database, name="add_models_to_database"),
    path('show_predictions/', views.show_predictions, name="show_predictions"),
    path('', views.index, name='index'),
]
