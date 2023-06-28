from django.db import models
from django.utils.text import slugify
from apps.products.managers import ProductManager


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price_uzs = models.PositiveIntegerField()
    description = models.CharField(max_length=1200)
    image = models.ImageField(upload_to='product-main-images')
    slug = models.SlugField(max_length=255, unique=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = ProductManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title_uz

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)
    

class Parameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Parameter'
        verbose_name_plural = 'Parameters'
    

class ProductSliderImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product-slider-images')

    def __str__(self) -> str:
        return self.product.title
    
    class Meta:
        verbose_name = 'ProductSliderImage'
        verbose_name_plural = 'ProductSliderImages'


class Document(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='product-documents')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        