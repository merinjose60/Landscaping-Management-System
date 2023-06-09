# Generated by Django 4.1.5 on 2023-02-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landscape_app', '0004_servicesaddmodel_delete_addservicesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddServicesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=50)),
                ('services', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ServicesAddModel',
        ),
    ]
