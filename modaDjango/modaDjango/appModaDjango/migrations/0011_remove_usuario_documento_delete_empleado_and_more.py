# Generated by Django 4.1.7 on 2023-05-16 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appModaDjango', '0010_usuario_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='documento',
        ),
        migrations.DeleteModel(
            name='empleado',
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
