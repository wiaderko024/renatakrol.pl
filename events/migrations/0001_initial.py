# Generated by Django 4.0.4 on 2022-04-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(default='')),
                ('time', models.DateTimeField()),
                ('place', models.TextField(default='')),
                ('polish_date', models.CharField(blank=True, editable=False, max_length=128, null=True)),
            ],
        ),
    ]
