# Generated by Django 4.2.3 on 2023-07-20 07:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0005_user_accounts_last_activity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_accounts",
            name="status",
            field=models.BooleanField(null=True, verbose_name="وضعیت"),
        ),
    ]