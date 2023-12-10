# Generated by Django 5.0 on 2023-12-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria', models.IntegerField()),
                ('data_de_criação', models.DateField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]