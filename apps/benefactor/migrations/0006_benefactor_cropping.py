# Generated by Django 3.0.5 on 2020-04-06 20:34

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('benefactor', '0005_auto_20200406_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefactor',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '255x255', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
    ]