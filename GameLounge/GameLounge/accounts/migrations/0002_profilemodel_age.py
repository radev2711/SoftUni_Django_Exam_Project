# Generated by Django 4.2.3 on 2023-07-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profilemodel",
            name="age",
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]