# Generated by Django 3.0.5 on 2020-04-12 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='receiver_email',
            new_name='email',
        ),
    ]
