from django.shortcuts import render

def homepage(response):
    return render(response, "hangout/home.html", {})
