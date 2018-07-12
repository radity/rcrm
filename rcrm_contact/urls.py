from django.contrib.auth.decorators import login_required
from django.urls import path
from rcrm_contact.views import ContactCreateView, ContactDeleteView, ContactDetailView,\
    ContactListView, ContactEditView,\
    AddressCreateView, AddressEditView, AddressDeleteView, \
    EmailCreateView, EmailEditView, EmailDeleteView, \
    PhoneCreateView, PhoneEditView, PhoneDeleteView, \
    SocialProfileCreateView, SocialProfileEditView, SocialProfileDeleteView, \
    DynamicCreateView, DynamicEditView, \
    contact_import, contact_export

app_name = 'Contacts'

urlpatterns = [
    # Contact
    path('', login_required(ContactListView.as_view()), name='Contact'),
    path('add/', login_required(ContactCreateView.as_view()), name='Contact_Create'),
    path('<int:pk>/', login_required(ContactDetailView.as_view()), name='Contact_Detail'),
    path('<int:pk>/edit/', login_required(ContactEditView.as_view()), name='Contact_Edit'),
    path('<int:pk>/delete/', login_required(ContactDeleteView.as_view()), name='Contact_Delete'),
    # Contact Import-Export
    path('import/', login_required(contact_import), name='Contact_Import'),
    path('export/', login_required(contact_export), name='Contact_Export'),
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
    # DynamicTab
    path('<int:pk>/dynamic/add/', login_required(DynamicCreateView.as_view()), name='Dynamic_Create'),
    path('dynamic/<int:pk>/', login_required(DynamicEditView.as_view()), name='Dynamic_Edit'),
]
