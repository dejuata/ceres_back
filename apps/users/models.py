from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password')

        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 1)

        if extra_fields.get('role') != 1:
            raise ValueError('Superuser must have role of Global Admin')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        (1, 'Admin'),
        (2, 'Manager'),
        (3, 'Field manager'),
        (4, 'Operator')
    )

    AUTH_PROVIDERS = {
        'google': 'google',
        'email': 'email'
    }

    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Apellidos")
    id_card = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cedula")
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False, default=2)
    birthdate = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    phone = models.CharField(max_length=50, blank=True, null=False, verbose_name="Celular")
    avatar_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Foto")
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
