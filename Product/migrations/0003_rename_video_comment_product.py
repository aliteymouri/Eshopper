# Generated by Django 4.1.4 on 2022-12-23 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='video',
            new_name='product',
        ),
    ]
