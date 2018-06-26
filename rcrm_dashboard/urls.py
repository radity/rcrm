from django.contrib.auth.decorators import login_required
from django.urls import path
from rcrm_dashboard.views import ContactView, HomeView

app_name = 'Dashboard'


urlpatterns = [
    path('', login_required(HomeView.as_view()), name='Home'),
    path('contact/', login_required(ContactView.as_view()), name='Contact'),
]