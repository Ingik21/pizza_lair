from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="offer-index"),
    path('<int:id>', views.get_offer_by_id, name="offer-detail"),
    path('2f1', views.two_for_one_offer, name='offer-2f1')

]
