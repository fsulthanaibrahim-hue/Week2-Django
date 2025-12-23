from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
    path('booking/', views.booking, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),
]
