# Generated by Django 3.2.10 on 2022-01-29 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220128_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-create_at'], 'verbose_name': 'productos', 'verbose_name_plural': 'productos'},
        ),
    ]
