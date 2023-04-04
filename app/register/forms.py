from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MauDangKi(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]
