# Generated by Django 4.1 on 2023-01-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('MobileNo', models.CharField(max_length=40)),
                ('Address', models.CharField(max_length=30)),
                ('Courses', models.TextField()),
                ('Salary', models.TextField()),
            ],
        ),
    ]
