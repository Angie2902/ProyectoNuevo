# Generated by Django 3.1.7 on 2021-04-10 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tuluayork', '0002_auto_20210410_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='estado',
        ),
    ]
