from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from pizza.models import MenuPizzas as pizza
from offer.models import Offer
from pizza.models import PizzaToppings
from pizza.models import PizzaImage

from pizza.forms.pizza_form import PizzaCreateForm
from pizza.models import Pizza as pizza
from offer.models import Offer
from pizza.models import PizzaCategory
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


def create_pizza(request):
    if request.method == 'POST':
        form = PizzaCreateForm(data=request.POST)
        if form.is_valid():
            pizza = form.save()
            pizza_image = PizzaImage(image=request.POST['image'], pizza=pizza)
            pizza_image.save()
            return redirect('candy-index')
    else:
        form = PizzaCreateForm()
    return render(request, 'pizza/create_pizza.html', {'from': form})
