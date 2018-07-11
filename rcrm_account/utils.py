from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import activate, deactivate
from django.urls import reverse_lazy

from rcrm_contact.models import Contact


# Create your views here.


class AccountControlViewMixin(object):
    def get_object(self, queryset=None):
        obj = super(AccountControlViewMixin, self).get_object()
        if not obj.account == self.request.user.account:
            raise Http404
        return obj


class AccountControlViewMixinTwo(object):
    def get_object(self, queryset=None):
        obj = super(AccountControlViewMixinTwo, self).get_object()
        if not obj.account == self.request.user.account or obj.is_deleted is True:
            raise Http404
        return obj


class AccountControlViewMixinThree(object):
    def get_object(self, queryset=None):
        obj = super(AccountControlViewMixinThree, self).get_object()
        if not obj.contact.account == self.request.user.account:
            raise Http404
        return obj


class AccountControlViewMixinFour(object):
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        contact = get_object_or_404(Contact, id=id)
        if not contact.account == self.request.user.account:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class UserAccountControlViewMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.account:
            return HttpResponseRedirect(reverse_lazy('Accounts:Account'))
        return super().dispatch(request, *args, **kwargs)


class LocaleMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            language_code = request.user.language
        else:
            if request.META.get('HTTP_ACCEPT_LANGUAGE'):
                language_code = request.META.get('HTTP_ACCEPT_LANGUAGE').split(',')[0]
            else:
                language_code = 'en'
        activate(language_code)
        response = self.get_response(request)
        deactivate()
        return response