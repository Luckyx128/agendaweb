# Generated by Django 5.0 on 2024-09-22 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_agenda_data_ini'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='nome',
            field=models.CharField(default='agenda', max_length=200),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='peso',
            field=models.IntegerField(),
        ),
    ]
