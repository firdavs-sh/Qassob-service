# Generated by Django 3.1.13 on 2022-09-03 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220902_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=200, null=True)),
                ('Familiya', models.CharField(max_length=200, null=True)),
                ('Email', models.EmailField(max_length=200, null=True)),
                ('telefon', models.CharField(max_length=200, null=True)),
                ('taklif', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
