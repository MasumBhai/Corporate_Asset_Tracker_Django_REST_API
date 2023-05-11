from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Asset_Tracker.views import CompanyViewSet, DeviceViewSet, SubscriberViewSet, SubscriptionViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'subscribers', SubscriberViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # for swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
