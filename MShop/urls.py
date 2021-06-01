from django.urls import path
from MShop.views import shop, cart, checkout


urlpatterns = [
    # path('', HomeView, name='homeview'),
    path('', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]