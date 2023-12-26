from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    type = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    given_max_qty = models.IntegerField()
    total_qty = models.IntegerField()

    def __str__(self):
        return self.name
