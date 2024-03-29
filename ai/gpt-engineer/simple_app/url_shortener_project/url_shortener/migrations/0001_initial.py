# Generated by Django 4.2.6 on 2023-10-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URL",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_url", models.URLField(unique=True)),
                ("url_hash", models.CharField(max_length=6, unique=True)),
                ("clicks", models.IntegerField(default=0)),
            ],
        ),
    ]
