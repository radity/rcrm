from django.views.generic import TemplateView
from rcrm_account.utils import UserAccountControlViewMixin


# Create your views here.


class HomeView(UserAccountControlViewMixin, TemplateView):
    """This view is for dashboard screen"""
    template_name = 'dashboard/pages/home.html'
