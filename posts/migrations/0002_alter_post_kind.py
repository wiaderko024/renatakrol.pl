# Generated by Django 4.0.4 on 2022-09-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='kind',
            field=models.CharField(choices=[('PILATES', 'PILATES'), ('GŁOS', 'GŁOS'), ('ŻYCIE', 'ŻYCIE'), ('YOGA', 'YOGA')], max_length=32),
        ),
    ]
