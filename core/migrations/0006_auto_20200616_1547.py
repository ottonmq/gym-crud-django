# Generated by Django 3.0.7 on 2020-06-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='tipo',
            field=models.CharField(choices=[('Reclamo', 'Reclamo'), ('Sugerencia', 'Sugerencia'), ('Solicitud', 'Solicitud')], default='Sugerencia', max_length=100),
        ),
    ]
