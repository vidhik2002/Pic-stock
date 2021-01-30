from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def show_about_page(request):
    if request.method == "POST":
        return redirect('/')

    return render(request, "aboutus.html", {})


def home_page(request):
    return render(request, "homepage.html", {})
