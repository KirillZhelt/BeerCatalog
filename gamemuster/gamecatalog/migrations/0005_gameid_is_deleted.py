# Generated by Django 3.0.2 on 2020-01-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamecatalog', '0004_auto_20200129_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameid',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
