from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombres")

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Apellidos")
    id_card = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name="Cedula")
    birthdate = models.DateField(blank=True, null=True, verbose_name="Fecha de nacimiento")
    phone = models.CharField(max_length=50, blank=False, null=False, verbose_name="Celular")
    avatar_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Foto")

    ROLE = (
        (1, 'Administrativo'),
        (2, 'Operario'),
        (3, 'Jefe de Campo'),
    )

    current_role = models.IntegerField(choices=ROLE, blank=False, null=False, default=1, verbose_name="Cargo")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
