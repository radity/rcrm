from django.contrib.auth.decorators import login_required
from django.urls import path

from rcrm_employee.views import EmployeeCreateView, EmployeeDeleteView, EmployeeDetailView, \
    EmployeeListView, EmployeeEditView,\
    AddressCreateView, AddressEditView, AddressDeleteView, \
    EmailCreateView, EmailEditView, EmailDeleteView, \
    PhoneCreateView, PhoneEditView, PhoneDeleteView, \
    SocialProfileCreateView, SocialProfileEditView, SocialProfileDeleteView,\
    employee_export

app_name = 'Employees'

urlpatterns = [
    path('', login_required(EmployeeListView.as_view()), name='Employee'),
    path('add/', login_required(EmployeeCreateView.as_view()), name='Employee_Create'),
    path('<int:pk>/', login_required(EmployeeDetailView.as_view()), name='Employee_Detail'),
    path('<int:pk>/edit/', login_required(EmployeeEditView.as_view()), name='Employee_Edit'),
    path('<int:pk>/delete/', login_required(EmployeeDeleteView.as_view()), name='Employee_Delete'),
    # Contact Import-Export
    path('export/', login_required(employee_export), name='Employee_Export'),
    # Address
    path('<int:pk>/address/add/', login_required(AddressCreateView.as_view()), name='Address_Create'),
    path('address/<int:pk>/', login_required(AddressEditView.as_view()), name='Address_Edit'),
    path('address/<int:pk>/delete/', login_required(AddressDeleteView.as_view()), name='Address_Delete'),
    # Email
    path('<int:pk>/email/add/', login_required(EmailCreateView.as_view()), name='Email_Create'),
    path('email/<int:pk>/', login_required(EmailEditView.as_view()), name='Email_Edit'),
    path('email/<int:pk>/delete/', login_required(EmailDeleteView.as_view()), name='Email_Delete'),
    # Phone
    path('<int:pk>/phone/add/', login_required(PhoneCreateView.as_view()), name='Phone_Create'),
    path('phone/<int:pk>/', login_required(PhoneEditView.as_view()), name='Phone_Edit'),
    path('phone/<int:pk>/delete/', login_required(PhoneDeleteView.as_view()), name='Phone_Delete'),
    # SocialProfile
    path('<int:pk>/social/add/', login_required(SocialProfileCreateView.as_view()), name='Social_Create'),
    path('social/<int:pk>/', login_required(SocialProfileEditView.as_view()), name='Social_Edit'),
    path('social/<int:pk>/delete/', login_required(SocialProfileDeleteView.as_view()), name='Social_Delete'),
]