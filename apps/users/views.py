from django.shortcuts import render, redirect


def account(request):
    if request.user.is_authenticated:
        print("User is logged in:", request.user.username)
        return render(request, 'users/account.html', {
        'isAuthenticated': True
        })
    else:
        print("User is not logged in.")
        return redirect('users:login')