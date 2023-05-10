from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="cart-index"),
    path('update_item/', views.update_item, name="update_item"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name='payment'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('review/', views.review, name='review'),
]
