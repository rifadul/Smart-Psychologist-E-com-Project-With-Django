# Generated by Django 3.1.7 on 2021-04-12 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0006_auto_20210411_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryaddress',
            name='receiver_name',
        ),
    ]