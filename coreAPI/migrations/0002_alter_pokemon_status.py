# Generated by Django 3.2.8 on 2021-10-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='status',
            field=models.CharField(choices=[('Normal', 'Normal'), ('Sub Legendary', 'Sub Legendary'), ('Legendary', 'Legendary'), ('Mythical', 'Mythical')], max_length=50),
        ),
    ]
