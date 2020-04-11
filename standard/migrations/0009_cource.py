# Generated by Django 3.0.4 on 2020-03-31 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0008_student_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('publish_Date', models.TimeField(auto_now_add=True)),
                ('standard', models.IntegerField()),
                ('description', models.TextField(max_length=200)),
                ('timings', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
    ]
