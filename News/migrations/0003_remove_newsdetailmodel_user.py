# Generated by Django 3.0.5 on 2023-12-13 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20231213_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsdetailmodel',
            name='user',
        ),
    ]
