from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from apps.birthdays.models import Birthday
from .forms import BirthdayForm

def home(request):
    if isinstance(request.user, AnonymousUser):
        return render(request, 'birthdays/home_no_account.html')
    
    birthdays = sorted(Birthday.objects.filter(user = request.user), key=lambda b: b.days_until_birthday())
    
    return render(request, 'birthdays/home.html', {
        'birthdays': birthdays,
        'user': request.user,
        
        })

def add_birthday(request):
    if request.method == 'POST':
        form = BirthdayForm(request.POST)
        if form.is_valid():
            birthday = form.save(commit=False)
            birthday.user = request.user
            birthday.save()
            messages.success(request, "Birthday added successfully!")
            return redirect('birthdays:add')
    else:
        form = BirthdayForm()
    return render(request, 'birthdays/add_birthday.html', {'form': form})

def edit_birthday(request, id):
    birthday =  Birthday.objects.get(id = id)

    if request.method == 'POST':
        form = BirthdayForm(request.POST, instance=birthday)  # Bind form with the birthday instance
        if form.is_valid():
            form.save()
            messages.success(request, "Birthday edited successfully!")
            return redirect('birthdays:home')
    
    else:
        form = BirthdayForm(instance=birthday)

    return render(request, 'birthdays/edit_birthday.html', {
        'form': form
    })

def delete_birthday(request, id):
    birthday =  Birthday.objects.get(id = id)
    birthday.delete()
    messages.success(request, "Birthday deleted successfully!")
    return redirect('birthdays:home')

def view_birthday(request, id):
    if isinstance(request.user, AnonymousUser):
        return render(request, 'birthdays/home_no_account.html')

    birthday =  Birthday.objects.get(id = id)
    return render(request, 'birthdays/view_birthday.html', {
        'birthday': birthday,
        })