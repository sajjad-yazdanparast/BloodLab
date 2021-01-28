from django.urls import path 
from .views import GetOrCreateOrders, GetOrCreateTestType, GetLabsDoingSpecificTestsAndReservasion, GetLabFreeTimeServices

urlpatterns = [
    path('get_or_create_order/', GetOrCreateOrders.as_view(), name='get-or-create-order'),
    path('get_or_create_testtype/', GetOrCreateTestType.as_view(), name='get-or-create-testtype'),
    path('get_labs_doing_specific_tests_and_reserve/', GetLabsDoingSpecificTestsAndReservasion.as_view(), name='get-labs-doing-specific-tests'),
    path('get_lab_free_time_services/', GetLabFreeTimeServices.as_view(), name='get-lab-free-time-services'),
]