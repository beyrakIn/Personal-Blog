# Generated by Django 3.1.6 on 2021-02-13 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20210213_2241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='body',
        ),
    ]