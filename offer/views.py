from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

import offer
from offer.models import Offer


# Create your views here.

def index(request):

    return render(request, 'offers/index.html', {'offers': Offer.objects.all().order_by('name')})


@login_required
def get_offer_by_id(request, id):
    return render(request, 'offers/offer_detail.html', {
        'offer': get_object_or_404(Offer, pk=id)})

