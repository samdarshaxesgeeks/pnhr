# Generated by Django 4.0.3 on 2022-04-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice1', '0004_auto_20220418_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]