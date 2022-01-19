# Generated by Django 3.2.10 on 2022-01-18 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220118_1518'),
        ('notifications', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='usuario'),
        ),
    ]
