# Generated by Django 2.0.3 on 2018-04-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180407_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]