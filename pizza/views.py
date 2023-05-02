from django.shortcuts import render
from pizza.models import MenuPizzas as pizza
from user.models import User
from pizza.models import PizzaToppings
from pizza.models import PizzaImage


# Create your views here.


def index(request):
    context = {'pizzas': pizza.objects.all().order_by('name')}
    return render(request, 'pizza/index.html', context)
