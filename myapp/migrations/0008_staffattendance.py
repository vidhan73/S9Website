# Generated by Django 4.1 on 2023-01-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_classrecord_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staffattendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdminName', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('MobileNo', models.CharField(max_length=100)),
                ('Date', models.DateTimeField()),
                ('Course', models.CharField(max_length=100)),
                ('Attendance', models.CharField(max_length=100)),
            ],
        ),
    ]
