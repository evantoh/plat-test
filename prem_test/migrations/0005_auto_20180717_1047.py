# Generated by Django 2.0 on 2018-07-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prem_test', '0004_auto_20180717_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premier_users',
            name='last_Name',
            field=models.CharField(default='', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='premier_users',
            name='middle_Name',
            field=models.CharField(default='', max_length=32, null=True),
        ),
    ]