# Generated by Django 4.2.8 on 2023-12-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_nome', models.CharField(max_length=100)),
                ('adotante_nome', models.CharField(max_length=100)),
                ('data_adocao', models.DateField()),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('A', 'Aprovada'), ('R', 'Rejeitada')], max_length=1)),
            ],
        ),
    ]
