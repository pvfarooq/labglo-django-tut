from django.db import DatabaseError

from .models import Account

withdraw_amount = 1000

# request from internet banking
def withdraw_money_internet(request, withdraw_amount):
    user = request.user

    account = Account.objects.get(user=user)
    account.balance -= withdraw_amount
    account.save()


# request from mobile app
def withdraw_money_mobile(request, withdraw_amount):
    user = request.user

    account = Account.objects.get(user=user)
    account.balance -= withdraw_amount
    account.save()


def proper_method(request, withdraw_amount):
    user = request.user
    try:
        # get the account of the user and lock until the transaction is complete;to block other transactions
        account = Account.objects.select_for_update().get(user=user)
        account.balance -= withdraw_amount
        account.save()
    except DatabaseError:
        return "Another transaction is in progress"
