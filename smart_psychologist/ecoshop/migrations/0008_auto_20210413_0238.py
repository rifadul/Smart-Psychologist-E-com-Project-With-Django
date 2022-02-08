# Generated by Django 3.1.7 on 2021-04-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoshop', '0007_auto_20210413_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('On The Way', 'On The Way')], default='Pending', max_length=100),
        ),
    ]