# Generated by Django 4.2.3 on 2023-07-29 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='0123467808', max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
