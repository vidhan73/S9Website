# Generated by Django 4.1 on 2023-01-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_staffattendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffattendance',
            name='Date',
            field=models.CharField(max_length=100),
        ),
    ]
