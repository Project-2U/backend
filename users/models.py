from django.db import models
from django.utils.translation import gettext_lazy as _
from profiles.models import UserProfile


# Create your models here.
class User(models.Model):
    name = models.CharField(_("nombre"), db_column="user_name", max_length=30)
    lastname = models.CharField(_('apellidos'), db_column="user_lastname", max_length=30)
    age = models.IntegerField(_('Edad'), db_column="user_age",null=True, blank=True)
    phone = models.CharField(_('teléfono/celular'), db_column="user_phone", max_length=10, null=True, blank=True)
    address = models.CharField(_('dirección'), db_column="user_address", max_length=64, null=True, blank=True)
    occupation = models.CharField(_('ocupación'), db_column="user_occupation", max_length=64, null=True, blank=True)
    create_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    update_at = models.DateTimeField(_('fecha de actualización'), auto_now=True)
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_('perfil de usuario'))

    class Meta:
        verbose_name = _("usuario")
        verbose_name_plural = _('usuarios')

    def __str__(self):
        return self.name + " " + self.lastname
