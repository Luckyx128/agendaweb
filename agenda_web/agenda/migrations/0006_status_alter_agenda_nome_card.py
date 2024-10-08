# Generated by Django 5.1.1 on 2024-09-24 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_alter_agenda_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='agenda',
            name='nome',
            field=models.CharField(default='agenda-2024-09-23 22:27:46.580912', max_length=200),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sprint', models.FloatField()),
                ('peso', models.CharField(max_length=2)),
                ('descricao', models.TextField()),
                ('id_agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.agenda')),
                ('id_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.status')),
            ],
        ),
    ]
