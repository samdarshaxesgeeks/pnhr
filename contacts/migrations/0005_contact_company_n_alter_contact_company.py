# Generated by Django 4.0.3 on 2022-04-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_remove_contact_is_individual_contact_indivisual'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company_n',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='company',
            field=models.BooleanField(default=False),
        ),
    ]
