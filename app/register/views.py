from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import MauDangKi

# Create your views here.


def register(response):
    if response.method == "POST":
        form = MauDangKi(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home_page")
        else:
            messages.info(response, "Dang ki khong thanh cong ")
            return render(response, "register/register.html", {"form": form})
    else:
        form = MauDangKi()

    messages.info(response, "Debug  " + "aaa" + str(response.POST))
    return render(response, "register/register.html", {"form": form})
