# Generated by Django 3.1.7 on 2021-04-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0005_auto_20210413_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('On The Way', 'On The Way'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Delivered', 'Delivered')], default='Pending', max_length=100),
        ),
    ]
