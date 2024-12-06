from django.db import models

# Create your models here.

# Categorical attribute models
class AgeGroup(models.Model):
    age_group = models.CharField(max_length=10, unique=True)

class Attrition(models.Model):
    attrition_status = models.CharField(max_length=3, unique=True)

class BusinessTravel(models.Model):
    travel_type = models.CharField(max_length=20, unique=True)

class Department(models.Model):
    department_name = models.CharField(max_length=50, unique=True)

class EducationField(models.Model):
    field_name = models.CharField(max_length=50, unique=True)

class Gender(models.Model):
    gender_type = models.CharField(max_length=6, unique=True)

class JobRole(models.Model):
    role_name = models.CharField(max_length=50, unique=True)

class MaritalStatus(models.Model):
    status = models.CharField(max_length=10, unique=True)

class SalarySlab(models.Model):
    slab = models.CharField(max_length=20, unique=True)

# Main Employee table
class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True, primary_key=True)  # Unique identifier
    age = models.IntegerField()
    daily_rate = models.IntegerField()
    distance_from_home = models.IntegerField()
    education = models.IntegerField()
    environment_satisfaction = models.IntegerField()
    employee_count = models.IntegerField()
    employee_number = models.IntegerField()
    hourly_rate = models.IntegerField()
    job_involvement = models.IntegerField()
    job_level = models.IntegerField()
    job_satisfaction = models.IntegerField()
    monthly_income = models.IntegerField()
    monthly_rate = models.IntegerField()
    num_companies_worked = models.IntegerField()
    percent_salary_hike = models.IntegerField()
    performance_rating = models.IntegerField()
    relationship_satisfaction = models.IntegerField()
    standard_hours = models.IntegerField()
    stock_option_level = models.IntegerField()
    total_working_years = models.IntegerField()
    training_times_last_year = models.IntegerField()
    work_life_balance = models.IntegerField()
    years_at_company = models.IntegerField()
    years_in_current_role = models.IntegerField()
    years_since_last_promotion = models.IntegerField()
    years_with_curr_manager = models.IntegerField()
    
    # Foreign Key Relationships
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)
    attrition = models.ForeignKey(Attrition, on_delete=models.CASCADE)
    business_travel = models.ForeignKey(BusinessTravel, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    education_field = models.ForeignKey(EducationField, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    job_role = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    salary_slab = models.ForeignKey(SalarySlab, on_delete=models.CASCADE)
    over_18 = models.CharField(max_length=1)
    overtime = models.BooleanField()


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['emp_id'], name='unique_employee')
        ]
