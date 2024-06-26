from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_app.routers.router_core import router as router_core



schema_view = get_schema_view(
    openapi.Info(
        title="ASTRO",
        default_version='v1',
        description="API"

    ),
    public=True,
    permission_classes=([permissions.AllowAny]),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('news/', include(router_core.urls)),
]
