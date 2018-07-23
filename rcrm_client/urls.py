from django.contrib.auth.decorators import login_required
from django.urls import path

from rcrm_client.views import ClientCreateView, ClientEditView, ClientDeleteView, \
    ClientListView, ClientDetailView,\
    ContactDeleteView, ContactAddView, ContactCreateView,\
    PhoneCreateView, PhoneEditView, PhoneDeleteView, \
    EmailCreateView, EmailEditView, EmailDeleteView, \
    AddressCreateView, AddressEditView, AddressDeleteView, \
    SocialCreateView, SocialEditView, SocialDeleteView

app_name = 'Clients'

urlpatterns = [
    path('', login_required(ClientListView.as_view()), name='Client'),
    path('add/', login_required(ClientCreateView.as_view()), name='Client_Create'),
    path('<int:pk>/', login_required(ClientDetailView.as_view()), name='Client_Detail'),
    path('<int:pk>/edit/', login_required(ClientEditView.as_view()), name='Client_Edit'),
    path('<int:pk>/delete/', login_required(ClientDeleteView.as_view()), name='Client_Delete'),
    # Contact
    path('<int:pk>/contact/add/', login_required(ContactAddView.as_view()), name='Contact_Add'),
    path('<int:pk>/contact/create/', login_required(ContactCreateView.as_view()), name='Contact_Create'),
    path('<int:pk>/contact/<int:contact_id>/delete/', login_required(ContactDeleteView.as_view()), name='Contact_Delete'),
    # Phone
    path('<int:pk>/phone/add/', login_required(PhoneCreateView.as_view()), name='Phone_Create'),
    path('<int:client_id>/phone/<int:pk>/', login_required(PhoneEditView.as_view()), name='Phone_Edit'),
    path('<int:client_id>/phone/<int:pk>/delete/', login_required(PhoneDeleteView.as_view()), name='Phone_Delete'),
    # Email
    path('<int:pk>/email/add/', login_required(EmailCreateView.as_view()), name='Email_Create'),
    path('<int:client_id>/email/<int:pk>/', login_required(EmailEditView.as_view()), name='Email_Edit'),
    path('<int:client_id>/email/<int:pk>/delete/', login_required(EmailDeleteView.as_view()), name='Email_Delete'),
    # Address
    path('<int:pk>/address/add/', login_required(AddressCreateView.as_view()), name='Address_Create'),
    path('<int:client_id>/address/<int:pk>/', login_required(AddressEditView.as_view()), name='Address_Edit'),
    path('<int:client_id>/address/<int:pk>/delete/', login_required(AddressDeleteView.as_view()), name='Address_Delete'),
    # Social
    path('<int:pk>/social/add/', login_required(SocialCreateView.as_view()), name='Social_Create'),
    path('<int:client_id>/social/<int:pk>/', login_required(SocialEditView.as_view()), name='Social_Edit'),
    path('<int:client_id>/social/<int:pk>/delete/', login_required(SocialDeleteView.as_view()), name='Social_Delete'),
]