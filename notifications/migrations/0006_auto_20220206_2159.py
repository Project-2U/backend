# Generated by Django 3.2.10 on 2022-02-07 02:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_alter_notification_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(auto_now_add=True, db_column='noti_date', default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(db_column='noti_title', default='Notification', max_length=25, verbose_name='titulo'),
        ),
    ]