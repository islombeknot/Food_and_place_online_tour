# Generated by Django 5.0.4 on 2024-04-07 01:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_foodplace_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='stars_given',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
