# Generated by Django 3.2 on 2021-05-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productprice',
            name='current_qty',
        ),
        migrations.RemoveField(
            model_name='productprice',
            name='selling_price',
        ),
        migrations.AddField(
            model_name='productprice',
            name='used_qty',
            field=models.IntegerField(default=0),
        ),
    ]
