# Generated by Django 3.0.5 on 2020-04-05 21:42

from django.db import migrations, models
import utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('beneficiary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='image',
            field=models.ImageField(upload_to=utils.helpers.upload_image),
        ),
    ]