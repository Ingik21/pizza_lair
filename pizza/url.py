from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="pizza-index"),
    path('<int:id>', views.get_pizza_by_id, name="pizza-detail"),
    path('create_pizza', views.create_pizza, name="create_pizza"),
    path('order-by-price', views.order_by_price, name='order_by_price')

]
