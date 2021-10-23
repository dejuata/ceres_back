from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.docs.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/zones/', include('apps.zones.urls')),
    path('api/labors/', include('apps.labors.urls')),
    path('api/products/', include('apps.products.urls')),
    path('api/schedules/', include('apps.schedules.urls')),
    path('api/home/', include('apps.home.urls')),
    path('api/worklogs/', include('apps.worklogs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
