from xml.etree.ElementInclude import include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from .views import login, PreceptorViewSet, ElementoComunicativoViewSet

router = DefaultRouter()
router.register(r'preceptores', PreceptorViewSet, basename='preceptores')
router.register(r'elementos', ElementoComunicativoViewSet, basename='elementos')

urlpatterns = [
    path('login/', login),
    ]

urlpatterns += router.urls
