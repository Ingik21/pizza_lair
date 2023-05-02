from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name="pizza-index"),
    path('<int:id>', views.get_pizza_by_id, name="pizza-detail"),
]
