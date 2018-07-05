from django.contrib.auth.decorators import login_required
from django.urls import path
from rcrm_dashboard.views import HomeView

app_name = 'Dashboard'


urlpatterns = [
    path('', login_required(HomeView.as_view()), name='Home'),
]