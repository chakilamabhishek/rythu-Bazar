# Generated by Django 2.2.1 on 2019-09-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rythubazarapp', '0005_auto_20190908_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='cropimage',
            field=models.ImageField(blank=True, upload_to='G:\\rythu\\rythubazar\\static'),
        ),
    ]
