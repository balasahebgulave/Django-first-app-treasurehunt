# Generated by Django 2.1 on 2018-09-07 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Treasure', '0004_auto_20180907_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasuregram',
            name='image',
        ),
    ]
