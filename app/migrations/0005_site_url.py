# Generated by Django 4.0.5 on 2022-06-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_sitemodel_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
