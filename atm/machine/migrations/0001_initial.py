# Generated by Django 3.2 on 2022-02-18 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('balance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.FloatField(max_length=200)),
                ('withdraw', models.FloatField(max_length=200)),
                ('transaction_history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine.user')),
            ],
        ),
    ]