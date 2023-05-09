from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from offer.models import Offer
from cart.models import Order, OrderItem, ContactInformation, ShippingAddress, OrderItemOffer
from pizza.models import Pizza
from user.models import Profile


# Create your views here.
@login_required
def index(request):
    return cart(request)


def update_item(request):
    data = json.loads(request.body)
    pizzaId = data.get('pizzaId')
    offerId = data.get('offerId')
    action = data.get('action')

    print('Action:', action)
    print('Pizza:', pizzaId)
    print('Offer:', offerId)

    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)

    if pizzaId:
        pizza = Pizza.objects.get(id=pizzaId)
        order_item, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)
    elif offerId:
        offer = Offer.objects.get(id=offerId)
        order_item, created = OrderItemOffer.objects.get_or_create(order=order, offer=offer)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    elif action == 'delete':
        order_item.quantity = 0

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse({'message': 'Item was added', 'quantity': order_item.quantity}, safe=False)


def update_item_offer(request):
    data = json.loads(request.body)
    offerId = data['offerId']
    action = data['action']
    print('Action:', action)
    print('Offer:', offerId)

    user = request.user.profile
    offer = Offer.objects.get(id=offerId)

    order, created = Order.objects.get_or_create(user=user, complete=False)

    order_item_offer, created = OrderItemOffer.objects.get_or_create(order=order, offer=offer)

    print(order_item_offer)

    if action == 'add':
        order_item_offer.quantity = (order_item_offer.quantity + 1)
    elif action == 'remove':
        order_item_offer.quantity = (order_item_offer.quantity - 1)

    elif action == 'delete':
        order_item_offer.quantity = 0

    order_item_offer.save()

    if order_item_offer.quantity <= 0:
        order_item_offer.delete()

    return JsonResponse(
        {'message': 'Item was added', 'name': order_item_offer.offer.name, 'id': order_item_offer.offer.id}, safe=False)


@login_required
def cart(request, url="cart/index.html"):
    print("test")

    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)

    order_items = order.orderitem_set.all()

    order_items_offer = order.orderitemoffer_set.all()

    print(order_items)
    print(order_items_offer.__dict__)

    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer}

    return render(request, url, context)


def checkout(request):
    user = request.user.profile
    order = Order.objects.get(user=user, complete=False)

    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()

    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer}
    return render(request, 'cart/checkout.html', context)


def payment(request):
    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)
    shipping_address = ShippingAddress.objects.get(order=order)
    contact_information = ContactInformation.objects.get(order=order)
    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()
    shipping_info = shipping_address.__dict__
    contact_info = contact_information.__dict__
    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer,
               'shipping_info': shipping_info, 'contact_info': contact_info}
    return render(request, 'cart/payment.html', context)


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

    context = {'order': order, 'contact_information': contact_information, 'shipping_address': shipping_address}
    return render(request, 'cart/payment.html', context)
