from django.http import Http404

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