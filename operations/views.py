from django.shortcuts import redirect, render
from django.views import View
from .models import Employee
import random
import string

# To generate random employee IDs
random_Employee_id = "EMP-" + "".join(
    random.choices(string.ascii_uppercase + string.digits, k=8)
)


# Create your views here.
class Index(View):
    def get(self, request):
        page = request.GET.get("page", "register")
        if page == "records":
            employee = Employee.objects.all()
            return render(request, "employee_list.html", {"employee": employee})

        return render(request, "employee_form.html")

    def post(self, request):
        employee_id = random_Employee_id
        print(employee_id)
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        department = request.POST.get("department")
        position = request.POST.get("position")
        date_of_birth = request.POST.get("date_of_birth")
        date_joined = request.POST.get("date_joined")
        salary = request.POST.get("salary")
        is_full_time = request.POST.get("is_full_time")
        if is_full_time:
            is_full_time = True
        else:
            is_full_time = False

        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        last_performance_review = request.POST.get("last_performance_review")

        save_Employee = Employee(
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            department=department,
            position=position,
            date_of_birth=date_of_birth,
            date_joined=date_joined,
            salary=salary,
            is_full_time=is_full_time,
            email=email,
            phone_number=phone_number,
            address=address,
            city=city,
            state=state,
            last_performance_review=last_performance_review,
        )

        save_Employee.save()
        return redirect("/?page=records")


class Delete(View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("/?page=records")


class Display(View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        return render(request, "employee_list.html", {"employee": employee})


class Update(View):
    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        return render(request, "employee_detail.html", {"employee": employee})

    def post(self, request, id):
        employee = Employee.objects.get(id=id)
        employee.first_name = request.POST.get("first_name")
        employee.last_name = request.POST.get("last_name")
        employee.department = request.POST.get("department")
        employee.position = request.POST.get("position")
        employee.date_of_birth = request.POST.get("date_of_birth")
        employee.date_joined = request.POST.get("date_joined")
        employee.salary = request.POST.get("salary")
        employee.is_full_time = request.POST.get("is_full_time")
        if employee.is_full_time:
            employee.is_full_time = True
        else:
            employee.is_full_time = False

        employee.email = request.POST.get("email")
        employee.phone_number = request.POST.get("phone_number")
        employee.address = request.POST.get("address")
        employee.city = request.POST.get("city")
        employee.state = request.POST.get("state")
        employee.last_performance_review = request.POST.get("last_performance_review")

        employee.save()
        return redirect("/?page=records")
