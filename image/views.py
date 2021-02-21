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
    cats = Category.objects.all()
    context = {'images': images, 'cats': cats}
    return render(request, "homepage.html", context)


def show_category_page(request, c):
    cats = Category.objects.all()
    images = Image_Create.objects.filter(cat__pk=c)
    print(cats.count())
    print(images.count())
    print(c)
    context = {'images': images, 'cats': cats}
    return render(request, "homepage.html", context)



