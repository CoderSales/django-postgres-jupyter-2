# Generated by Django 4.1.7 on 2023-03-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_alter_note_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="notes",
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
