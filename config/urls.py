from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/', include('apps.docs.urls')),
    # path('api/auth/', include('apps.account.urls')),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/zones/', include('apps.zones.urls')),
    path('api/labors/', include('apps.labors.urls')),
    path('api/schedules/', include('apps.schedules.urls')),
    path('api/home/', include('apps.home.urls')),
]
