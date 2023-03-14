# Generated by Django 4.1.5 on 2023-03-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landscape_app', '0008_addtowishlistmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addprojectsmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=150)),
                ('image', models.FileField(upload_to='landscape_app/static')),
            ],
        ),
    ]