from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class ManageUserProfile(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Los usuarios deben tener un correo electronico para el inicio de sesión.")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        super_user = self.create_user(email, password)
        super_user.is_admin = True
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.type = "MANAGER"
        super_user.save(using=self._db)
        return super_user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    class Type(models.TextChoices):
        CLIENT = 'CLIENT', _('cliente')
        MANAGER = 'MANAGER', _('administrador')

    type = models.CharField(_('tipo de usuario'), db_column="user_type", choices=Type.choices, max_length=15, null=True,
                            blank=True,
                            default='CLIENT')
    email = models.EmailField(_('correo'), unique=True, db_column="user_email")
    is_active = models.BooleanField(_('activo/inactivo'), default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(_('administrador'), default=False)

    USERNAME_FIELD = 'email'

    objects = ManageUserProfile()

    class Meta:
        verbose_name = _('perfil de usuario')
        verbose_name_plural = _('perfiles de usuario')
        ordering = ["-email"]

