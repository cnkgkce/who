# Generated by Django 4.0.5 on 2022-06-25 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_site_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='image',
            field=models.ImageField(blank=True, default='sites/default.jpg', null=True, upload_to='sites/'),
        ),
    ]
