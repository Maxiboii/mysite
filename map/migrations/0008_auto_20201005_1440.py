# Generated by Django 3.1.2 on 2020-10-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0007_auto_20201005_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='data',
            field=models.CharField(max_length=3000),
        ),
    ]
