# Generated by Django 3.2.5 on 2022-01-15 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_expense_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='date',
        ),
    ]
