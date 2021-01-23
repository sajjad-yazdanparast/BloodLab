from django.urls import path
from .views import Signin
urlpatterns = [
    path('signin/', Signin.as_view(), name='signin') ,
]