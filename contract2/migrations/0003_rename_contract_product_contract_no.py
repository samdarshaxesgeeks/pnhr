# Generated by Django 3.2.9 on 2022-04-22 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contract2', '0002_rename_service_status_contract_service_package'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='contract',
            new_name='contract_no',
        ),
    ]
