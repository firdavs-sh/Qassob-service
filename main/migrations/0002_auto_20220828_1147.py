# Generated by Django 3.1.13 on 2022-08-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rasm',
            field=models.FileField(upload_to='images/'),
        ),
    ]
