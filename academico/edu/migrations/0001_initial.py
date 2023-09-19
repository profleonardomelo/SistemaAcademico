# Generated by Django 4.2.5 on 2023-09-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('nome_aluno', models.CharField(max_length=200)),
                ('curso', models.CharField(max_length=100)),
                ('observacao', models.TextField()),
                ('data_matricula', models.DateField(auto_now_add=True, verbose_name='Data da matrícula')),
            ],
            options={
                'verbose_name': 'Matrícula de Aluno',
                'verbose_name_plural': 'Matrículas de Aluno',
                'ordering': ['nome_aluno'],
            },
        ),
    ]