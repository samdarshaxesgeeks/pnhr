# Generated by Django 3.1.12 on 2022-04-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_alter_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
