# Generated by Django 5.0.1 on 2024-04-24 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0049_alter_article_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 24, 12, 58, 59, 139440, tzinfo=datetime.timezone.utc)),
        ),
    ]
