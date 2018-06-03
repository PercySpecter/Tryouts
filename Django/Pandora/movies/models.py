from django.db import models


class Category(models.Model):
    genre = models.CharField(max_length = 250)
    year = models.CharField(max_length = 6)

    def __str__(self):
        return self.genre + " " + str(self.year)


class Movie(models.Model):
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    movie_title = models.CharField(max_length = 250)
    movie_poster = models.CharField(max_length=1000)
