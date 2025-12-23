from django.db import models
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='doctors'
    )

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    disease = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="bookings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.patient.name} → {self.doctor.name} on {self.date}"
