# Generated by Django 4.2.5 on 2023-09-04 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0012_rename_nome_veiculo_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='ano_fundacao',
            new_name='ano',
        ),
    ]
