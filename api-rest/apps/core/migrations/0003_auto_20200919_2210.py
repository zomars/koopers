# Generated by Django 3.1.1 on 2020-09-20 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200919_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.BooleanField(default=False),
        ),
    ]
