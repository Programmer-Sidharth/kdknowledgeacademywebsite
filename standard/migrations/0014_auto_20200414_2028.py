# Generated by Django 3.0.4 on 2020-04-14 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('standard', '0013_auto_20200413_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
