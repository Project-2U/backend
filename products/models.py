from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import  CloudinaryField

# Create your models here.
from categories.models import Category


class Product(models.Model):
    name = models.CharField(_('nombre'), max_length=254, db_column="prod_name")
    amount = models.PositiveIntegerField(_('cantidad'), db_column="prod_amount")
    price = models.PositiveIntegerField(_('precio'), db_column="prod_price")
    description = models.CharField(_('descripción'), max_length=254, blank=True, db_column="prod_description")

    trademark = models.CharField(_('marca'), max_length=64, null=True, blank=True, db_column="prod_trademark")
    warranty = models.CharField(_('garantía'), max_length=20, null=True, blank=True, db_column="prod_warranty")
    tutorial_url = models.URLField(_('link del tutorial'), null=True, blank=True, db_column="prod_tutorial")
    discount = models.PositiveSmallIntegerField(_('descuento'), null=True, blank=True, default=0,
                                                db_column="prod_discount")
    reference = models.CharField(_('referencia'), max_length=64, default="sin referencia", db_column="prod_reference",
                                 blank=True)
    create_at = models.DateTimeField(_('fecha de creación'), auto_now_add=True)
    update_at = models.DateTimeField(_('fecha de modificación'), auto_now=True)
    is_active = models.BooleanField(_('activo'), default=True)
    categories = models.ManyToManyField(Category, verbose_name=_("categorias"), related_name="products", blank=True)

    class Meta:
        verbose_name = _('productos')
        verbose_name_plural = _('productos')
        ordering = ["-create_at"]

    def __str__(self):
        return 'producto: ' + self.name


class ProductImage(models.Model):
    #path_image = CloudinaryField('image')
    path_image = models.ImageField(_('imagen'), upload_to='products/', db_column="prod_image")
    product = models.ForeignKey(Product, verbose_name=_('producto'), db_column='prod_id', on_delete=models.CASCADE,
                                related_name='images')

    class Meta:
        verbose_name = _('imagenes de producto')
        verbose_name_plural = _('imagenes de productos')
        ordering = ['product']

    def __unicode__(self):
        try:
            public_id = self.path_image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s>" % public_id
