from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('wishlist/add_to_bag/<int:item_id>/', views.add_wishlist_to_bag, name='add_wishlist_to_bag'),
    path('apply_gift_card/', views.apply_gift_card, name='apply_gift_card'),
]