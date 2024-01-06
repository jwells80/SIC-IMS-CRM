from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    criteria = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class CategoryCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)


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
