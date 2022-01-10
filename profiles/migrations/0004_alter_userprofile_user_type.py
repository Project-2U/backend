# Generated by Django 3.2.10 on 2022-01-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userprofile_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('CLIENT', 'cliente'), ('MANAGER', 'administrador')], default='CLIENT', max_length=15, null=True, verbose_name='tipo de usuario'),
        ),
    ]