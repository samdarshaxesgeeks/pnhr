# Generated by Django 4.0.3 on 2022-04-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0012_auto_20220418_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
