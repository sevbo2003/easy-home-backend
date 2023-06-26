from django.db import models
from apps.contact.validators import validate_uzb_phone_number
from apps.newsletter.tasks import send_news


class Newsletter(models.Model):
    phone_number = models.CharField(max_length=20, validators=[validate_uzb_phone_number])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
        ordering = ('-created_at',)


class Xabarnoma(models.Model):
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Xabarnoma'
        verbose_name_plural = 'Xabarnomalar'
        ordering = ('-created_at',)
    
    def save(self, *args, **kwargs):
        super(Xabarnoma, self).save(*args, **kwargs)
        message = self.message
        numbers = list(Newsletter.objects.all().values_list('phone_number', flat=True))
        send_news.apply_async(args=[numbers, message])
