from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from rcrm_account.views import LoginView, RegisterView


app_name = 'Accounts'


urlpatterns = [
    path('login/', LoginView.as_view(), name='Login'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('Dashboard:Home')), name='Logout'),
]