from django.contrib import admin
from django.urls import path, include
from core.views import whatsapp_webhook, MessageLogViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'messages', MessageLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('whatsapp/', whatsapp_webhook, name='whatsapp_webhook'),
]
