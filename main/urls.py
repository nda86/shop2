from django.urls import path, re_path
from .views import HomeView, ItemsList, cart_api_list

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('items', ItemsList.as_view(), name="items_list"),
    path('api/v1/carts', cart_api_list),
]
