from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    if register.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'users/register.html', {
        'form':UserCreationForm()})


def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')
