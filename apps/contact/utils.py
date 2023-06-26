from apps.contact.models import PhoneToken
import random
import string
from django.utils import timezone


def generate_token(phone_number):
    phone_token = PhoneToken.objects.create(phone_number=phone_number)
    token = ''.join(random.choices(string.digits, k=6))
    phone_token.token = token
    phone_token.expires_at = timezone.now() + timezone.timedelta(minutes=3)
    phone_token.save()
    return token
