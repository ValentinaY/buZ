# Generated by Django 2.1.7 on 2019-05-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal_app', '0002_auto_20190523_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo_electronico',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]