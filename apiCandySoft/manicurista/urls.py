from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.novedades import NovedadesViewSet
from .views.liquidaciones import LiquidacionViewSet

router = DefaultRouter()
router.register(r'novedades', NovedadesViewSet)
router.register(r'liquidaciones', LiquidacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]