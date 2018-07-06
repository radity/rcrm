from django.shortcuts import get_object_or_404

from rcrm_account.models import Account


def context_data(request):
    if request.user.is_authenticated and request.user.account:
        account = get_object_or_404(Account, id=request.user.account.id)
    else:
        account = None
    context = {
        "account": account,
    }
    return context

