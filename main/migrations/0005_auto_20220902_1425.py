# Generated by Django 3.1.13 on 2022-09-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220828_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='rasm',
            field=models.FileField(upload_to='media'),
        ),
    ]
