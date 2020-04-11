# Generated by Django 3.0.4 on 2020-03-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0005_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('standard', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
            ],
        ),
    ]
