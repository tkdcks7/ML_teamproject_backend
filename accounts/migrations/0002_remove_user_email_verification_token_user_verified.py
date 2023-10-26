# Generated by Django 4.2.6 on 2023-10-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="email_verification_token",
        ),
        migrations.AddField(
            model_name="user",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]