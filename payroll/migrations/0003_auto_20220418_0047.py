# Generated by Django 3.1.12 on 2022-04-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_alter_csv_id_alter_payrollrecord_id_alter_payslip_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payrollrecord',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
