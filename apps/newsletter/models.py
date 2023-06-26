from django.db import models
from apps.contact.validators import validate_uzb_phone_number


class Newsletter(models.Model):
    phone_number = models.CharField(max_length=20, validators=[validate_uzb_phone_number])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = _('Foydalanuvchi')
        verbose_name_plural = _('Foydalanuvchilar')
        ordering = ('-created_at',)