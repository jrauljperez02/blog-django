# Generated by Django 2.2 on 2022-03-31 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0004_opinion_cellphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='cellphone',
            field=models.CharField(max_length=12, verbose_name='Cellphone'),
        ),
    ]
