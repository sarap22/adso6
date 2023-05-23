# Generated by Django 4.1.7 on 2023-05-16 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appModaDjango', '0011_remove_usuario_documento_delete_empleado_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(max_length=30)),
                ('clave', models.TextField(max_length=30)),
                ('documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appModaDjango.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('apellido', models.TextField(max_length=30)),
                ('correo', models.TextField(max_length=30)),
                ('celular', models.PositiveBigIntegerField(verbose_name='Teléfono celular')),
                ('rol', models.TextField(max_length=30)),
                ('documento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appModaDjango.usuario')),
            ],
        ),
    ]
