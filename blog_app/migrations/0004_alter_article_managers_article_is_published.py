# Generated by Django 5.0.1 on 2024-02-08 23:26

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_testi'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('mamad', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
