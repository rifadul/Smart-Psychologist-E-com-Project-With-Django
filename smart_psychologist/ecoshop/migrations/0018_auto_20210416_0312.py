# Generated by Django 3.1.7 on 2021-04-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0017_auto_20210416_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered')], default='Pending', max_length=100),
        ),
    ]
