# Generated by Django 3.2.5 on 2022-01-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_expense_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
