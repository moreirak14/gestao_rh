# Generated by Django 4.0.2 on 2022-03-02 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("funcionarios", "0004_alter_funcionario_empresa"),
    ]

    operations = [
        migrations.AddField(
            model_name="funcionario",
            name="imagem",
            field=models.ImageField(default=1, upload_to=""),
            preserve_default=False,
        ),
    ]