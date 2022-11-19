# Generated by Django 3.0 on 2022-11-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0008_couponcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='couponcode',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='couponcode',
            name='product',
        ),
        migrations.AddField(
            model_name='couponcode',
            name='discount_price',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='couponcode',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='couponcode',
            name='minimum_amount',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='couponcode',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]
