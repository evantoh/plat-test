# Generated by Django 2.0 on 2018-07-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prem_test', '0009_premier_users_branch_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premier_users',
            name='branch_key',
            field=models.CharField(default='', max_length=32, null=True),
        ),
    ]
