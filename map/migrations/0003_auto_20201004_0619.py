# Generated by Django 3.1.2 on 2020-10-04 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20201004_0617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestoday',
            old_name='population',
            new_name='oblast',
        ),
    ]
