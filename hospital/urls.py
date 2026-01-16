from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('departments/', views.departments, name='departments'),
    path('departments/list/', views.departments_list, name='departments_list'),
    path("departments/<int:department_id>/doctors/", views.department_doctors, name="department_doctors"),

    path("doctors/", views.all_doctors, name="all_doctors"),
    path('doctors/', views.doctors_list, name='doctors'),
    
    path('patients/', views.patients, name='patients'),
    path('patient/<int:id>/', views.patient_details, name='patient_details'),
    path('cancel/<int:id>/', views.cancel_appointment, name='cancel_appointment'),

    path('booking/', views.booking, name='booking'),
    path('booking-success/', views.booking_success, name='booking_success'),

    path('cancel/<int:id>/', views.cancel_appointment, name='cancel_appointment'),

]
