from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', include('apps.docs.urls')),
    path('api/auth/', include('apps.account.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/zones/', include('apps.zones.urls')),
    path('api/labors/', include('apps.labors.urls')),
    path('api/worklog/', include('apps.worklog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)