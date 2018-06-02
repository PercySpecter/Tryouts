
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>This is the Movies app homepage</h1>")
