# Generated by Django 4.2.3 on 2023-07-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamemodel",
            name="rating",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]