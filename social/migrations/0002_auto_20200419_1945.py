# Generated by Django 3.0.5 on 2020-04-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
    ]