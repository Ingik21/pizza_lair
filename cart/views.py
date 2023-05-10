from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import json

from offer.models import Offer
from cart.models import Order, OrderItem, ContactInformation, ShippingAddress, OrderItemOffer, ContactInformationForm
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
    action2 = data.get('action2')

    print('Action:', action)
    print('Pizza:', pizzaId)
    print('Offer:', offerId)
    print('Action2:', action2)

    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)


    order_item = None
    order_item_offer = None

    if pizzaId:
        pizza = Pizza.objects.get(id=pizzaId)
        order_item, created = OrderItem.objects.get_or_create(order=order, pizza=pizza)
    elif offerId:
        offer = Offer.objects.get(id=offerId)
        order_item_offer, created = OrderItemOffer.objects.get_or_create(order=order, offer=offer)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)

    if action == 'add' and order_item:
        order_item.quantity += 1
    elif action == 'remove' and order_item:
        order_item.quantity -= 1
    elif action == 'delete' and order_item:
        order_item.quantity = 0

    if order_item:
        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()

    if action2 == 'add-offer' and order_item_offer:
        order_item_offer.quantity += 1
    elif action2 == 'remove-offer' and order_item_offer:
        order_item_offer.quantity -= 1

    elif action2 == 'delete-offer' and order_item_offer:
        order_item_offer.quantity = 0

    if order_item_offer:
        order_item_offer.save()

        if order_item_offer.quantity <= 0:
            order_item_offer.delete()

    if not order_item and not order_item_offer:
        return JsonResponse({'message': 'Invalid request'}, status=400)

    return JsonResponse(
        {'message': 'Item was added', 'quantity': order_item.quantity if order_item else order_item_offer.quantity},
        safe=False)


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

    contact_information, created = ContactInformation.objects.get_or_create(user=user, order=order)

    print(contact_information)
    if request.method == 'POST':
        form = ContactInformationForm(request.POST)
        # Update the contact information fields with the submitted form data
        contact_information.name = form.cleaned_data['name']
        contact_information.email = request.POST.get('email')
        contact_information.address = request.POST.get('phone')
        contact_information.save()

        # Redirect the user to the order confirmation page
        return HttpResponseRedirect('cart/payment/')


    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer, 'contact_information': contact_information}
    return render(request, 'cart/checkout.html', context)


def payment(request):
    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)




    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()
    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer}
    return render(request, 'cart/payment.html', context)


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

    context = {'order': order, 'contact_information': contact_information, 'shipping_address': shipping_address}
    return render(request, 'cart/payment.html', context)
