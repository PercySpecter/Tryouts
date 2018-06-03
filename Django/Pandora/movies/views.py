
from django.http import HttpResponse
from .models import Category
from django.template import loader


def index(request):
    all_categories = Category.objects.all()
    template = loader.get_template("movies/index.html")
    context = {
        "all_categories": all_categories,
    }

    return HttpResponse(template.render(context, request))


def detail(request, category_id):
    return HttpResponse("<h2>Details for Category id:" + str(category_id) + "</h2>")