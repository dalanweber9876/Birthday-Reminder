from django.shortcuts import render


def account(request):
    return render(request, 'users/account.html')