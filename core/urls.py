from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Все маршруты из chats (по желанию можно добавить префикс)
    path('', include('apps.chats.urls')),

    # Документация и схема API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redos/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]
