from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", lambda request: redirect('store/', permanent=False)),
    path('auth/', include("auth.urls")),
    path('store/', include("store.urls")),
    path('dashboard/', include("dashboard.urls")),
    path('product/', include("product.urls")),
    path('accounts/', include('allauth.urls')),
    # path('admin_management/', include("admin_management.urls")),
    path('test/', include("test.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
