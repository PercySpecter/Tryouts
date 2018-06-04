
from django.http import Http404
from django.http import HttpResponse
from .models import Category
from django.shortcuts import render, get_object_or_404


def index(request):
    all_categories = Category.objects.all()
    return render(request, "movies/index.html", {"all_categories": all_categories})


def detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "movies/detail.html", {"category": category})


