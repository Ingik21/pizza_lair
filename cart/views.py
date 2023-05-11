from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

from cart.forms.cart_forms import ContactInformationForm
from cart.forms.payment_form import PaymentForm
from offer.models import Offer
from cart.models import Order, OrderItem, ContactInformation, ShippingAddress, OrderItemOffer, Payment
from pizza.models import Pizza


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
    order, created = Order.objects.get_or_create(user=user, complete=False)
    try:
        contact = ContactInformation.objects.filter(order=order).last()
    except ContactInformation.DoesNotExist:
        contact = None
    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()

    if request.method == 'POST':

        form = ContactInformationForm(data=request.POST)
        if form.is_valid():
            contact_ = form.save(commit=False)
            contact_.order_id = order.id
            contact_.save()
            return redirect('create_payment')
    else:
        print("else")
        form = ContactInformationForm(instance=contact)
        print(contact)
    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer, 'form': form}
    return render(request, 'cart/checkout.html', context)


def payment(request):
    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user.id, complete=False)
    contact = ContactInformation.objects.filter(order=order).last()
    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()

    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer, 'contact': contact}
    return render(request, 'cart/payment.html', context)


def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

    context = {'order': order, 'contact_information': contact_information, 'shipping_address': shipping_address}
    return render(request, 'cart/payment.html', context)


def create_contact(request):

    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user, complete=False)
    contact_ = ContactInformation.objects.filter(order=order.user.id).last()
    order_items = order.orderitem_set.all()

    if request.method == 'POST':
        print(request.POST)
        form = ContactInformationForm(data=request.POST, instance=contact_)
        if form.is_valid():
            contact_ = form.save(commit=False)
            contact_.order_id = order.id
            contact_.save()
            print(contact_)
            return redirect('create_payment')
    else:
        form = ContactInformationForm(instance=contact_)
        print(form.initial)
        return render(request, 'cart/checkout.html', {'form': form})

    return render(request, 'cart/checkout.html', {'form': ContactInformationForm(instance=contact_)})


def create_payment(request):
    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user.id, complete=False)
    contact = ContactInformation.objects.filter(order=order).last()
    try:
        payment = Payment.objects.filter(order=order).last()
    except Payment.DoesNotExist:
        payment = None
    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()

    if request.method == 'POST':
        form = PaymentForm(data=request.POST)
        if form.is_valid():
            payment_ = form.save()
            payment_.order_id = order.id
            payment_.save()
            return redirect('review')
    else:
        form = PaymentForm(instance=payment)
    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer,
               'form': form, 'contact': contact}
    return render(request, 'cart/payment.html', context)

def review(request):
    user = request.user.profile
    order, created = Order.objects.get_or_create(user=user.id, complete=False)
    order_items = order.orderitem_set.all()
    order_items_offer = order.orderitemoffer_set.all()
    payment_form = Payment.objects.filter(order=order).last()
    contact_form = ContactInformation.objects.filter(order=order).last()

    context = {'order_items': order_items, 'order': order, 'order_items_offer': order_items_offer,
               'payment_form': payment_form, 'contact_form': contact_form}
    return render(request, 'cart/review.html', context)
