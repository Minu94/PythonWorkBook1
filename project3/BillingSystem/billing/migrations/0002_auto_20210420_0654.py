# Generated by Django 3.2 on 2021-04-20 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('billnumber', models.AutoField(primary_key=True, serialize=False)),
                ('bill_date', models.DateField(auto_now=True)),
                ('customer_name', models.CharField(max_length=60)),
                ('phone_number', models.CharField(max_length=12)),
                ('bill_total', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='OrderLines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_qty', models.FloatField()),
                ('amount', models.FloatField()),
                ('bill_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.order')),
            ],
        ),
    ]
