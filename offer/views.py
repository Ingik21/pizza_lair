from django.shortcuts import render
from offer.models import Offer


# Create your views here.

def index(request):
    return render(request, 'offers/index.html', {'offers': Offer.objects.all().order_by('name')})
