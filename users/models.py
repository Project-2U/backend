from django.db import models
from django.utils.translation import gettext_lazy as _
from profiles.models import UserProfile

# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(_("nombre"), max_length=30)
    user_lastname = models.CharField(_('apellidos'),  max_length=30)
    user_birthday = models.DateTimeField(_('fecha de nacimiento'),null=True, blank=True)
    user_phone = models.CharField(_('telefono/celular'), max_length=10, null=True, blank=True)
    user_address= models.CharField(_('dirección'), max_length=64, null=True, blank=True)
    user_occupation =models.CharField(_('ocupación'), max_length=64, null=True, blank=True)
    create_at= models.DateTimeField(_('fecha de creación'),auto_now_add=True)
    update_at= models.DateTimeField(_('fecha de actualización'),auto_now=True)
    user_profile=models.OneToOneField(UserProfile, on_delete=models.CASCADE, verbose_name=_('perfil de usuario'))

    class Meta:
        verbose_name=_("usuario")
        verbose_name_plural=_('usuarios')
    def __str__(self):
        return self.user_name + " "+ self.user_lastname


