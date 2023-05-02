from django.shortcuts import render, get_object_or_404
from pizza.models import MenuPizzas as pizza
from user.models import User
from pizza.models import PizzaToppings
from pizza.models import PizzaImage


# Create your views here.


def index(request):
    context = {'pizzas': pizza.objects.all().order_by('name')}
    return render(request, 'pizza/index.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_detail.html', {
        'pizza': get_object_or_404(pizza, pk=id)})
