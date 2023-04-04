from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MyApiRegister

urlpatterns = [
    path("register/", MyApiRegister.as_view(), name="api_register"),
    path("token/", obtain_auth_token),
]
