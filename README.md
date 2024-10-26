# Employee Management System

### A Django application for managing employee data, with features for adding, viewing, updating, and deleting employee records.

#

# Features

- `Add Employees`: Register new employees with details like name, department, position, contact info, etc.

- `List Employees`: Display all employee records .

- `View Employees`: Display registered employees, along with their details seperately.

- `Update Employee Information`: Modify existing employee data.

- `Delete Employee Records`: Remove employees from the system.

#

# Setup

## Prerequisites

- Python 3.x
- Django
- SQLite3 (included with Django by default)

# Installation

1. Clone the repository:

```
git clone <repository-url>
cd <project-directory>
```

2. Run database migrations:

```
python manage.py migrate
```

3. Start the development server:

```
python manage.py runserver
```

5. Open your web browser and visit http://127.0.0.1:8000/

#

# Alternative

### To Create Django Project from scratch

1. To Create Django Project

```
python -m django startproject <project-name>
```

2. To create your application in Project

```
cd <project-directory>
python manage.py startapp <app-name>
```

3. Start Development Server

```
python manage.py runserver
```

4. Open your web browser and visit http://127.0.0.1:8000/.

5. To configure the templates go to `settings.py` and configure your template folder and the app in it.

#

# Models

### Employee

#### The Employee model represents an employee record with the following fields:

- `employee_id` (CharField): Unique identifier for the employee, auto-generated.
- `first_name` (CharField): First name of the employee.
- `last_name` (CharField): Last name of the employee.
- `department` (CharField): Department the employee works in.
- `position` (CharField): Job position/title of the employee.
- `date_of_birth` (DateField): Employee's birth date.
- `date_joined` (DateField): Date the employee joined the company.
- `salary` (DecimalField): Employee's salary.
- `is_full_time` (BooleanField): Employment status, full-time or part-time.
- `email` (EmailField): Unique email address of the employee.
- `phone_number` (CharField): Contact number.
- `address` (TextField): Home address.
- `city` (CharField): City of residence.
- `state` (CharField): State of residence.
- `last_performance_review` (DateTimeField): Date of the last - performance review (optional).

#

# Views

1. Index: Handles listing and registration.

   - `GET /`: Shows the registration form (employee_form.html).
   - `GET /?page=records`: Lists all employees (employee_list.html).
   - `POST /`: Saves new employee data from the form.

2. Delete: Deletes an employee record by ID.

   - `GET /delete/<id>`: Deletes the specified employee record and redirects to the records page.

3. Display: Displays details of a specific employee.

   - `GET /display/<id>`: Renders employee_list.html with details of the specified employee.

4. Update: Updates an existing employee record.

   - `GET /update/<id>`: Displays the employee details for editing in employee_detail.html.
   - `POST /update/<id>`: Updates the specified employee record and saves changes.

#

# Templates

1. `employee_form.html`: Form for registering a new employee.
2. `employee_list.html`: Displays a list of all employee records or the details of a specific employee.
3. `employee_detail.html`: Form for updating an existing employee's information.

### Generating a Unique Employee ID

An employee ID is generated automatically using a random combination of uppercase letters and digits, prefixed with "EMP-".

#

## Usage

- `Register a New Employee`: Go to the root URL / to fill in the employee details form. Submit the form to save the new employee record.
- `List Employees`: Visit /?page=records to view all employee records.
- `Update Employee`: Click on an employee in the list, modify their details, and save the changes.
- `Delete Employee`: Select an employee from the list and delete the record permanently.

#

## Database

`SQLite3` is used for the default database, configured in settings.py. The Employee model fields map to columns in the database.

#
