# Generated by Django 3.2 on 2022-02-22 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='withdraw',
        ),
        migrations.RemoveField(
            model_name='user',
            name='balance',
        ),
        migrations.AddField(
            model_name='transactions',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]