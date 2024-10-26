from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_joined = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_full_time = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    last_performance_review = models.DateTimeField(null=True, blank=True)
