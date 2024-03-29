# Generated by Django 4.2.9 on 2024-01-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='active',
        ),
        migrations.AddField(
            model_name='productimage',
            name='thumbnail',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='productvariantprice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productvariantprice',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='variant',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
