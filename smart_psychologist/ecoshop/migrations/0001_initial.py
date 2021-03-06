# Generated by Django 3.1.7 on 2021-04-04 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.PositiveIntegerField()),
                ('discount_price', models.PositiveIntegerField(blank=True, null=True)),
                ('product_description', models.TextField(max_length=1000)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='uploads/product_images/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecoshop.productcategory')),
            ],
        ),
    ]
