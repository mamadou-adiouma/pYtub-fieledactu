# Generated by Django 5.1.6 on 2025-03-26 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("filedactuapp", "0003_messages_reponse_to"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messages",
            name="reponse_to",
            field=models.ForeignKey(
                default="no renseigné",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="filedactuapp.messages",
            ),
        ),
    ]
