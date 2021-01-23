from django.urls import path
from .views import UserSignup, BloodExpertSignup, LabSignup, TimeServiceRegistery
urlpatterns = [
    path('user_signup/', UserSignup.as_view(), name='user-signup') ,
    path('blood_expert_signup/', BloodExpertSignup.as_view(), name = 'expert-signup') ,
    path('lab_signup/', LabSignup.as_view(), name = 'lab-signup') ,
    path('time_service_registery/', TimeServiceRegistery.as_view(), name = 'time-service-registery') ,
]