# Generated by Django 4.1 on 2023-02-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_ifestivals_iinstitute_itopper'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('salary', models.IntegerField(max_length=400)),
                ('Date', models.DateField()),
                ('Amount', models.IntegerField(max_length=400)),
            ],
        ),
    ]
