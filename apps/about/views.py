from rest_framework import viewsets
from apps.about.models import Experience, TeamMember
from apps.about.serializers import ExperienceSerializer, TeamMemberSerializer
from rest_framework.response import Response
from rest_framework import status



class ExperienceViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Experience.objects.all().last()
        serializer = ExperienceSerializer(queryset)
        return Response(serializer.data)


class TeamMemberViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = TeamMember.objects.all()
        serializer = TeamMemberSerializer(queryset, many=True)
        return Response(serializer.data)
    