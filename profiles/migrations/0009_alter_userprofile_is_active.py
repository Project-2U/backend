# Generated by Django 3.2.10 on 2022-02-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_userprofile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='activo/inactivo'),
        ),
    ]
