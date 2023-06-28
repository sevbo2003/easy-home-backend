from django.db import models
from apps.service.managers import ServiceManager


class Service(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='service')
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)
    objects = ServiceManager()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ('-created_at',)


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='service')


class KeyFeatures(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='key_features')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    