# Generated by Django 3.1.7 on 2021-04-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0012_auto_20210415_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Delivered', 'Delivered'), ('On The Way', 'On The Way'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='Pending', max_length=100),
        ),
    ]
