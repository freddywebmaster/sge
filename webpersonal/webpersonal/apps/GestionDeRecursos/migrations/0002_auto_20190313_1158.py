# Generated by Django 2.1.7 on 2019-03-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionDeRecursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='Parentesco',
            field=models.CharField(choices=[('P', 'Padre'), ('M', 'Madre'), ('T', 'Tío/a'), ('A', 'Abuelo/a'), ('H', 'Hermano/a'), ('O', 'Otro')], default='P', max_length=1),
        ),
    ]