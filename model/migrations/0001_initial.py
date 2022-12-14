# Generated by Django 3.2.15 on 2022-08-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('joining_month', models.CharField(max_length=10)),
                ('joining_year', models.CharField(max_length=4)),
            ],
        ),
    ]
