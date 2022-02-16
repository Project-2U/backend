# Generated by Django 3.2.10 on 2022-02-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20220129_0945'),
        ('categories', '0004_auto_20220129_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='categorias', to='products.Product', verbose_name='productos'),
        ),
    ]
