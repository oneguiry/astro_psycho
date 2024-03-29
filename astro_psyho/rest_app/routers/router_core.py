from rest_framework import routers
from rest_app.viewsets.news import NewsViewSet

router = routers.DefaultRouter()
router.register('news', NewsViewSet, basename='news')
