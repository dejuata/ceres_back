from django.urls import path
from apps.authentication.views import (
    RegisterView, LogoutAPIView, VerifyEmail,
    LoginApiView, SetNewPasswordAPIView, RequestPasswordResetEmail,
    PasswordTokenCheckAPI, GoogleSocialAuthView)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginApiView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('google/', GoogleSocialAuthView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name="password-reset-confirm"),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name="password-reset-complete")
]
