from django.db import models

class Category(models.Model):
    actor = models.CharField(max_length = 250)
    year = models.IntegerField()
    movie_poster = models.CharField(max_length = 1000)

    def __str__(self):
        return self.actor + " " + str(self.year)


class Movie(models.Model):
    category = models.ForeignKey(Category , on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    movie_title = models.CharField(max_length = 250)
