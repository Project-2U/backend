from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Product


# Create your models here.


class Category(models.Model):
    name = models.CharField(_("nombre"), db_column="cat_name", max_length=64)
    description = models.CharField(_('descripcion'), db_column="cat_description", max_length=254, blank=True, null=True)
    create_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    update_at = models.DateTimeField(_('fecha de actualización'), auto_now=True)

    products = models.ManyToManyField(Product, verbose_name=_("productos"), related_name="categorias", blank=True, null="True")

    class Meta:
        verbose_name = _("categoria")
        verbose_name_plural = _("categorias")

    def __str__(self):
        return self.name

