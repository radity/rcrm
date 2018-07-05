from django.views.generic import TemplateView


# Create your views here.


class HomeView(TemplateView):
    """This view is for dashboard screen"""
    template_name = 'pages/home.html'
