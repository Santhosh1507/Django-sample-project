from django.urls import path
from . import views

urlpatterns = [
    path("myapp/", views.my_app, name="my_app"),
    path('', views.add_item, name='add_item'),
    path('item-list/', views.item_list, name='item_list'),
]