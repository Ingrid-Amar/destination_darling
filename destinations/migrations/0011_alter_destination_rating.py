# Generated by Django 4.2.8 on 2023-12-13 04:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("destinations", "0010_alter_destination_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="destination",
            name="rating",
            field=models.IntegerField(
                default=3,
                validators=[
                    django.core.validators.MaxValueValidator(5),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]