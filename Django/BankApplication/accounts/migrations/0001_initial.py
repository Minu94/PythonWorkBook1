# Generated by Django 3.1.7 on 2021-03-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personname', models.CharField(max_length=100)),
                ('accno', models.CharField(max_length=15, unique=True)),
                ('actype', models.CharField(max_length=120)),
                ('balance', models.IntegerField(default=30000)),
                ('phonenumber', models.CharField(max_length=12, unique=True)),
                ('mpin', models.CharField(max_length=6, unique=True)),
            ],
        ),
    ]
