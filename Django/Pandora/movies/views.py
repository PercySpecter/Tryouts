
from django.http import HttpResponse
from .models import Category


def index(request):
    all_categories = Category.objects.all()
    html = ""
    for category in all_categories:
        url = "/movies/" + str(category.id) + "/"
        html += "<a href = " + url + ">" + category.actor + "</a><br>"

    return HttpResponse(html)


def detail(request, category_id):
    return HttpResponse("<h2>Details for Category id:" + str(category_id) + "</h2>")