# Generated by Django 4.1 on 2023-01-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_staffregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffregistration',
            name='Address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='staffregistration',
            name='Salary',
            field=models.CharField(max_length=30),
        ),
    ]