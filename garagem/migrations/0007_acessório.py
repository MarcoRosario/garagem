# Generated by Django 4.2.4 on 2023-08-31 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0006_delete_autor_delete_livro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessório',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
