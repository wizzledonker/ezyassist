# Generated by Django 2.1.5 on 2019-05-04 03:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assist', '0006_auto_20190429_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistancerequest',
            name='lodge_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]