# Generated by Django 4.1.2 on 2022-11-25 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_profile_age_alter_profile_height_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
    ]
