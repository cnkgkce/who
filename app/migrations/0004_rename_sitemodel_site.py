# Generated by Django 4.0.5 on 2022-06-24 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_sitemodel_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteModel',
            new_name='Site',
        ),
    ]
