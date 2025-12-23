from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Doctor, Patient, Booking

def home(request):
    return render(request, 'hospital/home.html')

def departments(request):
    # Fetch all departments with their doctors
    departments = Department.objects.prefetch_related('doctor_set').all()
    return render(request, 'hospital/departments.html', {'departments': departments})

def doctors(request):
    doctors = Doctor.objects.select_related('department').all()
    return render(request, 'hospital/doctors.html', {'doctors': doctors})

def patients(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patients.html', {'patients': patients})

def booking(request):
    doctors = Doctor.objects.all()
    if request.method == "POST":
        patient_name = request.POST['patient_name']
        age = request.POST['age']
        disease = request.POST['disease']
        doctor_id = request.POST['doctor']
        date = request.POST['date']
        phone = request.POST['phone']

        doctor = get_object_or_404(Doctor, id=doctor_id)
        patient = Patient.objects.create(name=patient_name, age=age, disease=disease)
        Booking.objects.create(patient=patient, doctor=doctor, date=date, phone=phone)

        return redirect('booking_success')

    return render(request, 'hospital/booking.html', {'doctors': doctors})

def booking_success(request):
    return render(request, 'hospital/booking_success.html')
