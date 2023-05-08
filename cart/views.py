from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json

from cart.models import Order, OrderItem
from pizza.models import Pizza
from user.models import Profile



# Create your views here.
@login_required
def index(request):
    return cart(request)

def update_item(request):
    data = json.loads(request.body)
    pizzaId = data['pizzaId']
    action = data['action']
    print('Action:', action)
    print('Pizza:', pizzaId)


    user = request.user.profile
    pizza = Pizza.objects.get(id=pizzaId)

    order, created = Order.objects.get_or_create(user=user, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()



    if order_item.quantity <= 0:
        order_item.delete()



    return JsonResponse({'message': 'Item was added',  'quantity': order_item.quantity, 'name': order_item.pizza.name, 'price': order_item.pizza.base_price},safe=False)



@login_required
def cart(request):
    print("test")

    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)

    order_items = order.orderitem_set.all()

    print(order_items)






    context = {'order_items': order_items, 'order': order}


    return render(request, 'cart/index.html', context)

