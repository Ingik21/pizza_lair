from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from pizza.forms.pizza_form import PizzaCreateForm
from pizza.models import Pizza as pizza
from offer.models import Offer
from pizza.models import PizzaCategory
from pizza.models import PizzaImage


# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        pizzas = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'base_price': x.base_price,
            'firstImage': x.pizzaimage_set.first().image
        } for x in pizza.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': pizzas})

    order_by = request.GET.get('order_by')
    pizzas = pizza.objects.all()
    category = request.GET.get('category')

    if category:
        pizzas = pizzas.filter(category__name=category)

    if order_by == 'name':
        pizzas = pizzas.order_by('name')
    elif order_by == 'base_price':
        pizzas = pizzas.order_by('base_price')

    context = {'pizzas': pizzas}
    return render(request, 'pizza/index.html', context)


@login_required
def get_pizza_by_id(request, id):
    return render(request, 'pizza/pizza_detail.html', {
        'pizza': get_object_or_404(pizza, pk=id)})





@login_required
def create_pizza(request):
    if request.method == 'POST':
        form = PizzaCreateForm(data=request.POST)
        if form.is_valid():
            pizza_ = form.save()
            pizza_image = PizzaImage(image=request.POST['image'], pizza=pizza_)
            pizza_image.save()
            return redirect('pizza-index')
    else:
        form = PizzaCreateForm()
    return render(request, 'pizza/create_pizza.html', {'form': form})


def order_by_price(request):
    return index(request)


def order_by_name(request):
    return index(request)


def filter_by_category(request):
    return index(request)