# Generated by Django 4.2.4 on 2023-09-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_datauser'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=60)),
                ('lname', models.CharField(max_length=60)),
            ],
        ),
    ]
