# Generated by Django 4.1 on 2023-01-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_staffregistration_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=100)),
                ('Batch', models.CharField(max_length=100)),
                ('Board', models.CharField(max_length=100)),
                ('Time', models.CharField(max_length=100)),
            ],
        ),
    ]
