from django.shortcuts import render, redirect, get_object_or_404
from .models import Department, Doctor, Patient, Booking
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'hospital/home.html')


def all_doctors(request):
    query = request.GET.get('q', '')  # get the search query
    if query:
        doctors = Doctor.objects.filter(
            name__icontains=query
        ) | Doctor.objects.filter(
            department__name__icontains=query
        )
    else:
        doctors = Doctor.objects.all()
    return render(request, "hospital/doctors.html", {
        "doctors": doctors,
        "query": query
    })


def departments(request):
    departments = Department.objects.prefetch_related('doctors').all()
    print(departments)
    for i in departments:
        print(i)
    return render(request, 'hospital/departments.html', {'departments': departments})

def department_doctors(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    doctors = Doctor.objects.filter(department=department)
    context = {
        'department': department,
        'doctors': doctors
    }
    return render(request, 'hospital/department_doctors.html', context)

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


@login_required
def departments_list(request):
    departments = Department.objects.all()
    return render(request, 'hospital/departments_list.html', {'departments': departments})

