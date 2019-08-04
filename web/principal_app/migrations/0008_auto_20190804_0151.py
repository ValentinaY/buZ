# Generated by Django 2.2.1 on 2019-08-04 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal_app', '0007_auto_20190523_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acuerdo',
            fields=[
                ('placas', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('direccionInicial', models.CharField(max_length=50)),
                ('direccionFinal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('cedula', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo_electronico', models.CharField(max_length=60, unique=True)),
                ('contrasena', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('cedula', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo_electronico', models.CharField(max_length=60, unique=True)),
                ('contrasena', models.CharField(max_length=128)),
                ('acuerdoAsociado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal_app.Acuerdo')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placas', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tecnomecanica', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Pista',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='conductor',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal_app.Vehiculo'),
        ),
        migrations.AddField(
            model_name='acuerdo',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal_app.Vehiculo'),
        ),
    ]