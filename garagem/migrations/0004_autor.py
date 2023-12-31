# Generated by Django 4.2.4 on 2023-08-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0003_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
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
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                "verbose_name": "Autor",
                "verbose_name_plural": "Autores",
            },
        ),
    ]
