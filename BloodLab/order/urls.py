from django.urls import path 
from .views import GetOrCreateOrders

urlpatterns = [
    path('get_or_create_order/', GetOrCreateOrders.as_view(), name='get-or-create-order'),
]