# Generated by Django 3.2.10 on 2022-02-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productimage_path_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='path_image',
            field=models.ImageField(db_column='prod_image', upload_to='products/', verbose_name='imagen'),
        ),
    ]
