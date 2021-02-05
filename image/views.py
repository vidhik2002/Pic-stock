from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def show_about_page(request):
    if request.method == "POST":
        return redirect('/')

    return render(request, "aboutus.html", {})


def show_home_page(request):
    images = Image_Create.objects.all()
    cat = Category.objects.all()
    context = {'images': images, 'cat': cat}
    return render(request, "homepage.html", context)


def category_page(request):
    pass
