
# HR Analytics UI

This is the frontend of the HR Analytics application built with Angular. The project integrates with a Django REST API backend to manage and analyze employee data.

## Project Structure
```bash
UI-hr_analytics/hr-analytics-ui/ 
├── src/ 
│ ├── app/ 
│ ├── assets/ 
│ ├── environments/ 
│ └── index.html 
├── angular.json 
├── package.json 
└── README.md
```
## Features

- **Employee Management**: Add, view, edit, and delete employee records.
- **CSV Import/Export**: Upload employee data via CSV files and export it as needed.
- **Analytics Dashboard**: Display HR metrics using charts and graphs.

## Technologies Used

- **Angular**: Framework for building the UI.
- **Bootstrap**: For styling and responsiveness.
- **ngx-bootstrap**: For additional UI components.

## Prerequisites For Angular-frontend

- Node.js (v14+)
- Angular CLI (v15+)
- npm (Node Package Manager)
---
## Installation - Angular

1. Clone the repository:
   ```bash
   git clone https://github.com/harshalshinde437/IIT-Capstone-project.git
   cd UI-hr_analytics/hr-analytics-ui/
   ```
2. install dependency:
    ```bash
    npm install
    ```
3. Start the development server:
    ```bash
    ng serve -o
    ```
The application will be accessible at http://localhost:4200.


## Building the Project
1. To create a production build, run:
    ```bash
    ng build --prod
    ```
The output will be stored in the dist/ directory.

## For Contribution

1. Fork the repository.
2. Create a new branch:
```bash
git checkout -b feature-name
```
3. Commit your changes:
```bash
git commit -m 'Add feature-name'
```
4. Push to the branch:
```bash
git push origin feature-name
```
5. Create a pull request.

---

# HR Analytics Backend

This is the backend for the HR Analytics application, built using Django and Django REST Framework (DRF). It provides APIs to manage employee data and perform analytics, and integrates with the Angular frontend.

## Project Structure
```bash
hr_analytics/ 
├── hr_analytics/ 
│ ├── init.py 
│ ├── asgi.py 
│ ├── settings.py 
│ ├── urls.py 
│ ├── wsgi.py 
├── employee/ 
│ ├── migrations/ 
│ ├── init.py 
│ ├── admin.py 
│ ├── apps.py 
│ ├── models.py 
│ ├── serializers.py 
│ ├── tests.py 
│ ├── views.py 
├── manage.py 
└── README.md
```

## Features

- RESTful API for managing employee data.
- Import/export functionality for CSV files.
- Integration with the Angular frontend.
- Analytics endpoints for HR metrics.

## Technologies Used

- **Django**: Backend framework.
- **Django REST Framework (DRF)**: For building APIs.
- **SQLite3**: Default database (can be switched to others like PostgreSQL).
- **Python**: Programming language.
- **CSV Handling**: For importing/exporting data.

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtualenv (optional but recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/harshalshinde437/IIT-Capstone-project.git
   cd hr_analytics/
   ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
The application will be accessible at http://127.0.0.1:8000.

---
## API Endpoints
Here are some of the key API endpoints provided by the backend:

- Employee Management:
    - GET /api/employees/ - List all employees.
    - POST /api/employees/ - Add a new employee.
    - GET /api/employees/<id>/ - Get details of a specific employee.
    - PUT /api/employees/<id>/ - Update an employee's details.
    - DELETE /api/employees/<id>/ - Delete an employee.

- CSV Operations:
    - POST /api/employees/import/ - Import employees from a CSV file.
    - GET /api/employees/export/ - Export employee data to a CSV file.

- Analytics:
    - GET /api/analytics/ - Get key HR metrics and visualizations.

## Testing
1. Run the tests to ensure everything works correctly:
```bash
python manage.py test
```
2. Deployment
- Install a production-ready web server like Gunicorn:
    ```bash
    pip install gunicorn
    ```
3. Update the settings.py for production:
```bash
Set DEBUG = False
Add allowed hosts in ALLOWED_HOSTS.
```
- Use a reverse proxy like Nginx or Apache to serve the application.

## Google Colab Link:
Link: https://colab.research.google.com/drive/1g4etWZSXuOHxjRoL5CqrSIGl0xX5t1dS#scrollTo=R5gqpmuPf9gj

## Contribution
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m 'Add feature-name'
    ```
4. Push to the branch:
    ```bash
    git push origin feature-name
    ```
5. Create a pull request.

## Contributor

- Harshal Shinde (G23AI2045) 
- Rajendra Panda (G23AI2030) 
- Aishwarya Salunkhe (G23AI2031) 
- Yash Engendala (G23AI2064) 
- Mounika V S (G23AI2099) 
- Sandip Shaw (G23AI2095)


