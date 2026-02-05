from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ReportViewSet, FlagViewSet, BanViewSet, WarningViewSet

router = DefaultRouter()
router.register('reports', ReportViewSet, basename='report')
router.register('flags', FlagViewSet, basename='flag')
router.register('bans', BanViewSet, basename='ban')
router.register('warnings', WarningViewSet, basename='warning')

urlpatterns = [
    path('', include(router.urls)),
]
