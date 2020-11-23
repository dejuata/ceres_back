from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from apps.account.views import RegisterView, LoginView
from django.conf.urls import url, include


urlpatterns = [
    path('token', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
]
