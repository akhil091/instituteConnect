# Generated by Django 3.1.4 on 2020-12-23 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201223_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='image1',
            new_name='image',
        ),
    ]
