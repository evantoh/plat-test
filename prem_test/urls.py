from django.urls import path

from . import views

urlpatterns = [
    path('data/', views.premium_users, name='premium_users'),
    path('getcsv/', views.get_csv, name='get_csv'),
]