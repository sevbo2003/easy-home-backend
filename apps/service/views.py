from rest_framework.viewsets import ModelViewSet
from apps.service.models import Service
from apps.service.serializers import ServiceSerializer, ServiceRetrieveSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    http_method_names = ['get', 'head', 'options']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        return ServiceSerializer
    