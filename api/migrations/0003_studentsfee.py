# Generated by Django 3.2.5 on 2022-01-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('fee', models.CharField(max_length=30)),
            ],
        ),
    ]