# Generated by Django 4.0.5 on 2022-07-18 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.city', verbose_name='city'),
        ),
    ]
