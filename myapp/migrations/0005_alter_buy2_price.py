# Generated by Django 4.2.4 on 2023-09-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_buy2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy2',
            name='price',
            field=models.CharField(max_length=60),
        ),
    ]
