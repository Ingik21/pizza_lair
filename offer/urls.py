from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="offer-index"),
    path('<int:id>', views.get_offer_by_id, name="offer-detail"),
<<<<<<< HEAD
    path('2f1', views.two_for_one_offer, name='offer-2f1'),
=======
    path('2f1', views.two_for_one_offer, name='offer-2f1')

>>>>>>> 5d958650c2dca2722e1ebcb4d9fdd9824e93516b
]
