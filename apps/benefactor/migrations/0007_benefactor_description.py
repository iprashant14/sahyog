# Generated by Django 3.0.5 on 2020-04-12 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benefactor', '0006_benefactor_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='benefactor',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
