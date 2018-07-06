import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import get_object_or_404

from rcrm_account.models import Account


def context_data(request):
    accounts = Account.objects.filter(is_active=True, is_deleted=False).values_list('name')
    account_list = json.dumps(list(accounts), cls=DjangoJSONEncoder)
    if request.user.is_authenticated and request.user.account:
        account = get_object_or_404(Account, id=request.user.account.id)
    else:
        account = None
    context = {
        "account": account,
        "account_list": account_list,
    }
    return context
    