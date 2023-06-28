from django.urls import path
from apps.about.views import ExperienceViewSet


urlpatterns = [
    path('experience/', ExperienceViewSet.as_view({'get': 'list'})),
]
