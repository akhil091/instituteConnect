# Generated by Django 3.1.4 on 2020-12-23 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201223_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='img_slider',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='innovation',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='sop',
            old_name='image',
            new_name='images',
        ),
    ]
