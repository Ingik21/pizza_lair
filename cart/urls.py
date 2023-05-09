from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="cart-index"),
    path('update_item/', views.update_item, name="update_item"),
    path('update_item_offer/', views.update_item_offer, name="update_item_offer"),


]
