# Generated by Django 3.1.6 on 2021-02-13 18:41

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]