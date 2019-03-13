# Generated by Django 2.1.7 on 2019-03-13 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellidos', models.CharField(max_length=100)),
                ('Nombres', models.CharField(max_length=100)),
                ('Documento', models.CharField(max_length=11)),
                ('FechaDeNacimiento', models.DateField()),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='m', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Sala', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellidos', models.CharField(max_length=100)),
                ('Nombres', models.CharField(max_length=100)),
                ('Documento', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asunto', models.CharField(max_length=150)),
                ('Detalle', models.CharField(max_length=1000)),
                ('Aprobado', models.BooleanField(default=False)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Permisos.Alumno')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Permisos.Curso')),
                ('Docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Permisos.Docente')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apellidos', models.CharField(max_length=100)),
                ('Nombres', models.CharField(max_length=100)),
                ('Documento', models.CharField(max_length=11)),
                ('Parentesco', models.CharField(choices=[('Pa', 'Padre'), ('Ma', 'Madre'), ('Ti', 'Tío/a'), ('Ab', 'Abuelo/a'), ('He', 'Hermano/a'), ('Ot', 'Otro')], default='Pa', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='Tutores',
            field=models.ManyToManyField(to='Permisos.Tutor'),
        ),
    ]
