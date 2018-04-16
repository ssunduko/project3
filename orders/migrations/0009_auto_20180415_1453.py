# Generated by Django 2.0.3 on 2018-04-15 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180410_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_Plate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=24)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=24)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=24)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='dinner_plate',
            name='item',
            field=models.ManyToManyField(to='orders.Item'),
        ),
        migrations.AddField(
            model_name='order',
            name='dinner_plates',
            field=models.ManyToManyField(to='orders.Dinner_Plate'),
        ),
        migrations.AddField(
            model_name='order',
            name='pastas',
            field=models.ManyToManyField(to='orders.Pasta'),
        ),
        migrations.AddField(
            model_name='order',
            name='salads',
            field=models.ManyToManyField(to='orders.Salad'),
        ),
    ]