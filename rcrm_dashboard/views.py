from django.views.generic import TemplateView

from rcrm_contact.models import Contact


# Create your views here.


class HomeView(TemplateView):
    """This view is for dashboard screen"""
    template_name = 'pages/home.html'


class ContactView(TemplateView):
    """This view is for contact list screen"""
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contacts'] = Contact.objects.filter(is_deleted=False)
        return context
