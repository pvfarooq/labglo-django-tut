# Generated by Django 4.1.2 on 2022-10-13 06:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0003_book_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="published_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
