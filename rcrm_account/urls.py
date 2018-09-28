from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView

from rcrm_account.views import (AccountView, AccountUserCreateView, AccountRequestCreateView, LoginView, RegisterView,
                                ForgotPasswordView, ResetPasswordView, ProfileView, UserAccountDeleteView,
                                AccountRequestAcceptView, AccountRequestDeclineView)

app_name = 'Accounts'


urlpatterns = [
    # Auth
    path('login/', LoginView.as_view(), name='Login'),
    path('register/', RegisterView.as_view(), name='Register'),
    path('password/forgot/', ForgotPasswordView.as_view(), name='Forgot_Password'),
    path('password/reset/<key>/', ResetPasswordView.as_view(), name='Reset_Password'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('Dashboard:Home')), name='Logout'),
    # Account
    path('', login_required(AccountView.as_view()), name='Account'),
    path('<int:pk>/logo', login_required(AccountView.as_view()), name='AccountLogo'),
    # Account User
    path('add/user/', login_required(AccountUserCreateView.as_view()), name='Account_Add_User'),
    path('<int:pk>/delete/', login_required(UserAccountDeleteView.as_view()), name='User_Delete'),
    # Account Request
    path('request/', login_required(AccountRequestCreateView.as_view()), name='Account_Request'),
    path('request/<int:pk>/', login_required(AccountRequestAcceptView.as_view()), name='Request_Accept'),
    path('request/<int:pk>/decline/', login_required(AccountRequestDeclineView.as_view()), name='Request_Decline'),
    # User Profile
    path('profile/', login_required(ProfileView.as_view()), name='User_Profile')
]
