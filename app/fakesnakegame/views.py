import os

from django.http import FileResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


def fakesnakegame(response):
    return render(response, "fakesnakegame/download.html", {})


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = "fakesnakegame.rar"
    # Define the full file path
    filepath = BASE_DIR + "/fakesnakegame/Files/" + filename
    # Open the file for reading content
    zip_file = open(filepath, "rb")
    return FileResponse(zip_file)
