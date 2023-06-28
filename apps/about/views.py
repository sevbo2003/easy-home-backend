from rest_framework import viewsets
from apps.about.models import Experience
from apps.about.serializers import ExperienceSerializer
from rest_framework.response import Response
from rest_framework import status



class ExperienceViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Experience.objects.all().last()
        serializer = ExperienceSerializer(queryset)
        return Response(serializer.data)