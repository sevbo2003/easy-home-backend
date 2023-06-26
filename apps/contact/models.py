from django.db import models
from apps.contact.validators import validate_uzb_phone_number

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, validators=[validate_uzb_phone_number])
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    