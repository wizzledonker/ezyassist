# Generated by Django 2.1.5 on 2019-03-21 02:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assist', '0002_auto_20190321_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
