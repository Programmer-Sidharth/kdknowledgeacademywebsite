# Generated by Django 3.0.4 on 2020-03-31 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0004_student_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]