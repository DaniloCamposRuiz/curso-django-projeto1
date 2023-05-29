from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.ImageField()
    preparation_time_unit = models.CharField(max_length=165)
    servings = models.ImageField()
    servings_unit = models.CharField(max_length=165)
    preparation_steps = models.TextField()
    preparation_steps = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')


# Create your models here.
