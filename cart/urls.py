from django.urls import path
from . import views
from .views import redirect_view

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('update_item/', views.update_item, name="update_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name='payment'),
    path('redirect/', redirect_view)
]
