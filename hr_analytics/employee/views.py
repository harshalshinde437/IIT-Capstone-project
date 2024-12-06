# Create your views here.
# employee/views.py

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Employee, AgeGroup, Attrition, BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, SalarySlab
from .serializers import EmployeeSerializer

# for csv functionality
from django.http import HttpResponse
from .models import *
import csv
import pandas as pd

class EmployeeAPIView(APIView):

    # GET method to fetch all employees or a single employee by emp_id
    def get(self, request, emp_id=None):
        if emp_id:
            # Fetch a specific employee by emp_id
            employee = get_object_or_404(Employee, emp_id=emp_id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Fetch all employees
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    # POST create new employee
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT update an employee by emp_id
    def put(self, request, emp_id):
        employee = get_object_or_404(Employee, emp_id=emp_id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE an employee by emp_id
    def delete(self, request, emp_id):
        employee = get_object_or_404(Employee, emp_id=emp_id)
        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ImportCSVView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Read CSV file
        file = request.FILES['file']
        data = pd.read_csv(file)

        imported_rows = 0
        skipped_rows = 0

        for _, row in data.iterrows():
            emp_id = row['EmpID']

            # Check if the record already exists
            if Employee.objects.filter(emp_id=emp_id).exists():
                skipped_rows += 1
                continue

            # Get or create objects for foreign key fields based on the data in the row
            age_group, _ = AgeGroup.objects.get_or_create(age_group=row['AgeGroup'])
            attrition, _ = Attrition.objects.get_or_create(attrition_status=row['Attrition'])
            business_travel, _ = BusinessTravel.objects.get_or_create(travel_type=row['BusinessTravel'])
            department, _ = Department.objects.get_or_create(department_name=row['Department'])
            education_field, _ = EducationField.objects.get_or_create(field_name=row['EducationField'])
            gender, _ = Gender.objects.get_or_create(gender_type=row['Gender'])
            job_role, _ = JobRole.objects.get_or_create(role_name=row['JobRole'])
            marital_status, _ = MaritalStatus.objects.get_or_create(status=row['MaritalStatus'])
            salary_slab, _ = SalarySlab.objects.get_or_create(slab=row['SalarySlab'])

            # Create the employee record
            Employee.objects.create(
                emp_id=emp_id,
                age=row['Age'],
                daily_rate=row['DailyRate'],
                distance_from_home=row['DistanceFromHome'],
                education=row['Education'],
                employee_count = row['EmployeeCount'],
                employee_number = row['EmployeeNumber'],
                environment_satisfaction=row['EnvironmentSatisfaction'],
                hourly_rate=row['HourlyRate'],
                job_involvement=row['JobInvolvement'],
                job_level=row['JobLevel'],
                job_satisfaction=row['JobSatisfaction'],
                monthly_income=row['MonthlyIncome'],
                monthly_rate=row['MonthlyRate'],
                num_companies_worked=row['NumCompaniesWorked'],
                percent_salary_hike=row['PercentSalaryHike'],
                performance_rating=row['PerformanceRating'],
                relationship_satisfaction=row['RelationshipSatisfaction'],
                standard_hours=row['StandardHours'],
                stock_option_level=row['StockOptionLevel'],
                total_working_years=row['TotalWorkingYears'],
                training_times_last_year=row['TrainingTimesLastYear'],
                work_life_balance=row['WorkLifeBalance'],
                years_at_company=row['YearsAtCompany'],
                years_in_current_role=row['YearsInCurrentRole'],
                years_since_last_promotion=row['YearsSinceLastPromotion'],
                years_with_curr_manager=row['YearsWithCurrManager'],
                age_group=age_group,
                attrition=attrition,
                business_travel=business_travel,
                department=department,
                education_field=education_field,
                gender=gender,
                job_role=job_role,
                marital_status=marital_status,
                salary_slab=salary_slab,
                over_18=row['Over18'],
                overtime=(row['OverTime'] == 'Yes')
            )

            imported_rows += 1

        return Response({
            "message": "CSV import completed",
            "imported_rows": imported_rows,
            "skipped_rows": skipped_rows
        }, status=status.HTTP_201_CREATED)



class ExportCSVView(APIView):
    def get(self, request):
        employees = Employee.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'EmpID',
            'Age',
            'AgeGroup',
            'Attrition',
            'BusinessTravel',
            'DailyRate', 
            'Department',
            'DistanceFromHome',
            'Education',
            'EducationField', 
            'EmployeeCount', 
            'EmployeeNumber', 
            'EnvironmentSatisfaction',
            'Gender',
            'HourlyRate',
            'JobInvolvement', 
            'JobLevel',
            'JobRole',
            'JobSatisfaction',
            'MaritalStatus',
            'MonthlyIncome',
            'SalarySlab', 
            'MonthlyRate',
            'NumCompaniesWorked',
            'Over18',
            'OverTime',
            'PercentSalaryHike', 
            'PerformanceRating',
            'RelationshipSatisfaction',
            'StandardHours',
            'StockOptionLevel', 
            'TotalWorkingYears',
            'TrainingTimesLastYear',
            'WorkLifeBalance',
            'YearsAtCompany', 
            'YearsInCurrentRole',
            'YearsSinceLastPromotion',
            'YearsWithCurrManager'
        ])

        for employee in employees:
            writer.writerow([
                employee.emp_id, 
                employee.age, 
                employee.age_group.age_group, 
                employee.attrition.attrition_status, 
                employee.business_travel.travel_type, 
                employee.daily_rate, 
                employee.department.department_name, 
                employee.distance_from_home, 
                employee.education, 
                employee.education_field.field_name, 
                employee.employee_count, 
                employee.employee_number, 
                employee.environment_satisfaction, 
                employee.gender.gender_type, 
                employee.hourly_rate, 
                employee.job_involvement, 
                employee.job_level, 
                employee.job_role.role_name, 
                employee.job_satisfaction, 
                employee.marital_status.status, 
                employee.monthly_income, 
                employee.salary_slab.slab, 
                employee.monthly_rate, 
                employee.num_companies_worked, 
                employee.over_18, 'Yes' if employee.overtime else 'No', 
                employee.percent_salary_hike,
                employee.performance_rating, 
                employee.relationship_satisfaction,
                employee.standard_hours,
                employee.stock_option_level, 
                employee.total_working_years,
                employee.training_times_last_year,
                employee.work_life_balance, 
                employee.years_at_company, 
                employee.years_in_current_role, 
                employee.years_since_last_promotion, 
                employee.years_with_curr_manager
            ])

        return response