# Generated by Django 4.2.4 on 2023-09-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='buy2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=60)),
                ('price', models.FloatField(default=0.0)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
    ]