from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('events',EventViewSet)
router.register('reports',ReportViewSet)
router.register('contact',ContactViewSet)
router.register('auditlogs',AuditLogViewSet)
router.register('gallery',GalleryViewSet)

urlpatterns=[
    path('',include(router.urls)),
]