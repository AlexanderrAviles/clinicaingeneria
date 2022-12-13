# Generated by Django 4.1 on 2022-12-12 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_paciente_examenes_alter_paciente_expediente_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genero",
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
                ("nombre", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="Prevision",
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
                ("nombre", models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name="paciente",
            name="prevision",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.prevision"
            ),
        ),
        migrations.AlterField(
            model_name="paciente",
            name="sexo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.genero"
            ),
        ),
    ]