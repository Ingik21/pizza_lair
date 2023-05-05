from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

from cart.models import Order, OrderItem
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


    customer = request.profile.user
    pizza = Pizza.objects.get(id=pizzaId)

    order, created = Order.objects.get_or_create(user=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()



    if orderItem.quantity <= 0:
        orderItem.delete()





    return JsonResponse('Item was added', safe=False)

def cart(request):

    if request.user.is_authenticated:
        user = request.Profile.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []

    context = {'items': items}

    return render(request, 'cart/index.html', context)

