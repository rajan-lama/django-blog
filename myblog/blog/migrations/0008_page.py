# Generated by Django 5.1.6 on 2025-02-15 15:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_rename_name_category_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField(null=True)),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "published_at",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("slug", models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
