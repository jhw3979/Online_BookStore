# Generated by Django 2.2.5 on 2020-11-21 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0012_auto_20201120_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Order_DP',
            field=models.IntegerField(default=0),
        ),
    ]
