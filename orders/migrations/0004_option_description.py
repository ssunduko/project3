# Generated by Django 2.0.3 on 2018-04-07 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180407_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=24),
            preserve_default=False,
        ),
    ]