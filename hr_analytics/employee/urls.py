# employee/urls.py

from django.urls import path
from .views import EmployeeAPIView, ExportCSVView, ImportCSVView

urlpatterns = [
    path('employees/import_csv/', ImportCSVView.as_view(), name='employee-import'),  # Import CSV
    path('employees/export_csv/', ExportCSVView.as_view(), name='employee-export'),  # Export CSV
    path('employees/', EmployeeAPIView.as_view(), name='employee-list'),  # GET all, POST
    path('employees/<str:emp_id>/', EmployeeAPIView.as_view(), name='employee-detail'),  # GET by emp_id, PUT, DELETE
]
