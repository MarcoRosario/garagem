# Generated by Django 4.2.4 on 2023-08-28 19:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("garagem", "0005_livro"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Autor",
        ),
        migrations.DeleteModel(
            name="Livro",
        ),
    ]
