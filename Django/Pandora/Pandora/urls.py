
from django.contrib import admin
from django.conf.urls import include , url
from . import views

urlpatterns = [
    url(r"^$", views.index, name = "index"),
    url(r'^admin/', admin.site.urls),
    url(r'^movies/', include("movies.urls")),
]
