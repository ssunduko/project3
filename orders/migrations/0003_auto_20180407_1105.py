# Generated by Django 2.0.3 on 2018-04-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180405_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='description',
        ),
        migrations.AddField(
            model_name='option',
            name='number_of_topings',
            field=models.IntegerField(default=0),
        ),
    ]