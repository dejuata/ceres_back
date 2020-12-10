from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', include('apps.docs.urls')),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/zones/', include('apps.zones.urls')),
    path('api/labors/', include('apps.labors.urls')),
<<<<<<< HEAD
    path('api/products/', include('apps.products.urls')),
    path('api/worklog/', include('apps.worklog.urls')),
=======
    path('api/schedules/', include('apps.schedules.urls')),
    path('api/home/', include('apps.home.urls')),
    path('api/worklogs/', include('apps.worklogs.urls')),
>>>>>>> 0f3e12bb6ddcfbb5df02ae2ea328043619cd4abb
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
