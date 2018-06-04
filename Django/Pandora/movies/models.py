from django.db import models


class Category(models.Model):
    actor = models.CharField(max_length = 250)

    def __str__(self):
        return self.actor


class Movie(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=250)
    movie_poster = models.CharField(max_length=1000)

    def __str__(self):
        return self.movie_title + "." + self.file_type
