from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)
        