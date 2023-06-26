from django.urls import path
from apps.newsletter.views import NewsletterViewSets


urlpatterns = [
    path('', NewsletterViewSets.as_view({'post': 'create'}), name='newsletter'),
]