from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pizza.models import MenuPizzas as pizza
from user.models import User
from pizza.models import PizzaToppings
from pizza.models import PizzaImage


# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [ {
            'id': pizza.id,
            'name': pizza.name,
            'description': pizza.description,
            'base_price': pizza.base_price,
            'firstImage': pizza.pizzaimage_set.first().image
        } for pizza in pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas })

    context = {'pizzas': pizza.objects.all().order_by('name')}
    return render(request, 'pizza/index.html', context)


def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_detail.html', {
        'pizza': get_object_or_404(pizza, pk=id)})
