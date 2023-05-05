from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

from cart.models import Order
from pizza.models import Pizza


# Create your views here.
@login_required
def index(request):
    return render(request, 'cart/index.html')

def update_item(request):
    data = json.loads(request.body)
    pizzaId = data['pizzaId']
    action = data['action']
    print('Action:', action)
    print('Pizza:', pizzaId)


    user = request.user.user
    pizza = Pizza.objects.get(id=pizzaId)

    return JsonResponse('Item was added', safe=False)

def cart(request):

    if request.user.is_authenticated:
        user = request.profile.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []

        context = {'items': items}

    return render(request, 'cart/index.html', context)

