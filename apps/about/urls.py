from django.urls import path
from apps.about.views import ExperienceViewSet, TeamMemberViewSet


urlpatterns = [
    path('experience/', ExperienceViewSet.as_view({'get': 'list'})),
    path('team/', TeamMemberViewSet.as_view({'get': 'list'})),
]
