# Generated by Django 4.2.3 on 2023-07-07 07:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tournaments", "0003_alter_tournamentmodel_prise"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tournamentmodel",
            name="participants",
            field=models.ManyToManyField(
                blank=True, default=None, null=True, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
