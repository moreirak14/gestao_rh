# Generated by Django 4.0.2 on 2022-02-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documentos", "0003_alter_documento_pertence"),
    ]

    operations = [
        migrations.AddField(
            model_name="documento",
            name="arquivo",
            field=models.FileField(default="", upload_to="documentos"),
            preserve_default=False,
        ),
    ]
