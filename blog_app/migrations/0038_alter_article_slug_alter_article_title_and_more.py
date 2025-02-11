# Generated by Django 5.0.1 on 2024-04-20 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0037_alter_article_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, db_collation='', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_collation='', max_length=50, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 20, 19, 53, 24, 380962, tzinfo=datetime.timezone.utc)),
        ),
    ]
