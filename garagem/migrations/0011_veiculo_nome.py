# Generated by Django 4.2.5 on 2023-09-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0010_veiculo_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='nome',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
