from django.shortcuts import render

# Create your views here.

pizzas = [
    {'name': 'Pepperoni', 'price': 1000},
    {'name': 'Hawaiian', 'price': 1400},
    {'name': 'Meat lover', 'price': 2000},
    {'name': 'Margarita', 'price': 900}
]


def index(request):
    return render(request, 'pizza/index.html', context={'pizzas': pizzas})
