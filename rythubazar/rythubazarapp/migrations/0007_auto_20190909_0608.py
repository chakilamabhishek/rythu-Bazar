# Generated by Django 2.2.1 on 2019-09-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rythubazarapp', '0006_auto_20190908_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='cropimage',
            field=models.ImageField(blank=True, default='', upload_to='G:\\rythu\\rythubazar\\static'),
        ),
    ]
