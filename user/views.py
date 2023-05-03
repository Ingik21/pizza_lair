from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from user.models import Profile
from user.forms.profile_form import ProfileForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()})

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html',{
        'form': ProfileForm(instance=profile)
    })


def login(request):
    return render(request, 'user/login.html')


def logout(request):
    return render(request, 'user/logout.html')
