# Generated by Django 3.1.6 on 2021-02-14 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0008_auto_20210214_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', django_editorjs.fields.EditorJsField(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]