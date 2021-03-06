# Generated by Django 3.2.4 on 2021-07-11 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analyses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="concentration",
            field=models.CharField(
                help_text="Valores das concentrações para cada absorbância fornecida             separados por vírgulas.",
                max_length=255,
                verbose_name="Concentrações",
            ),
        ),
    ]
