# Generated by Django 5.0.4 on 2024-04-07 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_remove_foodcomment_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcomment',
            name='comment',
            field=models.TextField(),
        ),
    ]
