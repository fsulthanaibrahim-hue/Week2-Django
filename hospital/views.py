from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Doctor, Patient, MedicalRecord
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from django.db.models import Q




def home(request):
    return render(request, 'hospital/home.html')


def all_doctors(request):
    query = request.GET.get('q', '')
    doctors = Doctor.objects.select_related('department')

    if query:
        doctors = doctors.filter(
            name__icontains=query
        ) | doctors.filter(
            department__name__icontains=query
        )

    return render(request, 'hospital/doctors.html', {'doctors': doctors, 'query': query})


def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctors.html', {'doctors': doctors})


def departments(request):
    departments = Department.objects.prefetch_related('doctors').all()
    return render(request, 'hospital/departments.html', {
        'departments': departments
    })


def department_doctors(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    doctors = Doctor.objects.filter(department=department)
    return render(request, 'hospital/department_doctors.html', {
        'department': department,
        'doctors': doctors
    })


@login_required(login_url='login')
def patients(request):
    query = request.GET.get('q', '')
    patients = Patient.objects.all()

    if query:
        patients = patients.filter(
            Q(name__icontains=query) |
            Q(disease__icontains=query)
        )

    return render(request, 'hospital/patients.html', {
        'patients': patients,
        'query': query
    })



@login_required(login_url='login')
def booking(request):
    doctors = Doctor.objects.all()

    if request.method == "POST":
        patient_name = request.POST['patient_name']
        age = request.POST['age']
        disease = request.POST['disease']
        doctor_id = request.POST.get('doctor')
        doctor = Doctor.objects.get(id=doctor_id)
        date = request.POST['date']
        phone = request.POST['phone']

        doctor = get_object_or_404(Doctor, id=doctor_id)

        patient = Patient.objects.create(
            name=patient_name,
            age=age,
            disease=disease
        )

        MedicalRecord.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            phone=phone
        )

        return redirect('booking_success')

    return render(request, 'hospital/booking.html', {
        'doctors': doctors
    })


@login_required(login_url='login')
def booking_success(request):
    return render(request, 'hospital/booking_success.html')


@login_required(login_url='login')
def departments_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
          Department.objects.create(name=name)
          return redirect("department_list")
        departmets = Department.objects.all()
        return render(request, 'hospital/departments_list.html', {
        'departments': departments
    })



@login_required(login_url='login')
def patient_details(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'hospital/patient_details.html', {
        'patient': patient
    })


@login_required(login_url='login')
def cancel_appointment(request, id):
    try:
        patient = Patient.objects.get(id=id)
        patient.delete()
    except Patient.DoesNotExist:
        pass

    return redirect('patients')
