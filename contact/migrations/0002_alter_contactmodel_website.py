# Generated by Django 3.2.9 on 2022-07-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
