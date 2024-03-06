from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    criteria = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Season(models.Model):
    season = models.CharField(max_length=25)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.season

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.season)
        super().save(force_insert, force_update, using, update_fields)


class Size(models.Model):
    size = models.CharField(max_length=25)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.size

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.size)
        super().save(force_insert, force_update, using, update_fields)


class CategoryCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    type = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    given_max_qty = models.IntegerField()
    total_qty = models.IntegerField()

    def __str__(self):
        return self.name
