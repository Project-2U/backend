# Generated by Django 3.2.10 on 2022-01-29 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220128_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-create_at'], 'verbose_name': 'usuario', 'verbose_name_plural': 'usuarios'},
        ),
    ]
