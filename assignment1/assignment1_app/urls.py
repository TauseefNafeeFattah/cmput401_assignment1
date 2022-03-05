from django.urls import path
from . import views

urlpatterns=[
    path('coffees',views.coffeelist),
    path('coffees/<int:pk>',views.coffee_detail),
]
