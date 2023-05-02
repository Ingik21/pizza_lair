from django.shortcuts import render
from user.models import User


# Create your views here.

def index(request):
    return render(request, 'offers/index.html', {'users': User.objects.all().order_by('name')})
