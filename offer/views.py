from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json


import offer
from offer.models import Offer
from pizza.models import Pizza as pizza


# Create your views here.

def index(request):
    return render(request, 'offers/index.html', {'offers': Offer.objects.all().order_by('name')})


@login_required
def get_offer_by_id(request, id):
    return render(request, 'offers/offer_detail.html', {
        'offer': get_object_or_404(Offer, pk=id)})



def two_for_one_offer(request):
    pizzas = pizza.objects.all()
    context = {'pizzas': pizzas}

    if request.method == 'POST':
        pizza1_id = request.POST.get('pizza1')
        pizza2_id = request.POST.get('pizza2')
        pizza1 = pizza.objects.get(id=pizza1_id)
        pizza2 = pizza.objects.get(id=pizza2_id)
        if int(pizza1.base_price) > int(pizza2.base_price):
            total_price = pizza1.base_price
        else:
            total_price = pizza2.base_price

        pizzaId = '2f1'

        context = {
            'id': '2f1'+str(pizza2.id)+str(pizza2.id),
            'pizza_1': pizza1.name,
            'pizza_2': pizza2.name,
            'total_price': total_price
        }

        return render(request, 'offers/index.html', context)

    return render(request, 'offers/2f1.html', context)


