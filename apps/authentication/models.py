from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


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
        if password is None:
            raise ValueError('Password should not be none')

        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


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

    email = models.EmailField(unique=True, db_index=True, verbose_name='Email')

    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Apellidos")
    id_card = models.CharField(max_length=50, blank=False, null=False, verbose_name="Cedula")
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False, default=2)
    birthdate = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    phone = models.CharField(max_length=50, blank=True, null=False, verbose_name="Celular")
    avatar_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Foto")
    date_joined = models.DateTimeField(auto_now_add=True)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
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
