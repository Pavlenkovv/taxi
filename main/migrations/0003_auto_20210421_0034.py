# Generated by Django 3.2 on 2021-04-20 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210420_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='in_what_time',
            field=models.CharField(max_length=100),
        ),
    ]
