# Generated by Django 2.2.1 on 2019-08-04 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal_app', '0012_trabajador_acuerdoasociado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acuerdo',
            name='hora',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='vehiculo',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='principal_app.Vehiculo'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='acuerdoAsociado',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='principal_app.Acuerdo'),
        ),
    ]
