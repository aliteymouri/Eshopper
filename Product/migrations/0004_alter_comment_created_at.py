# Generated by Django 4.1.4 on 2022-12-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_rename_video_comment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
