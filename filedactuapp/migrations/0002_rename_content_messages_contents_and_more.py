# Generated by Django 5.1.6 on 2025-03-25 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("filedactuapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="messages",
            old_name="content",
            new_name="contents",
        ),
        migrations.RenameField(
            model_name="messages",
            old_name="user",
            new_name="users",
        ),
    ]
