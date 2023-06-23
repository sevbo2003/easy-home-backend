from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="easy-home-backend API}}",
        default_version='v1.0.0',
        description="Backend for Easy Home application",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Apps
    path('api/v1/news/', include('apps.news.urls')),
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)