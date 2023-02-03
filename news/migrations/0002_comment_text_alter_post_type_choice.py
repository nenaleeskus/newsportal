# Generated by Django 4.1.6 on 2023-02-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=222, max_length=244),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='type_choice',
            field=models.CharField(choices=[('NW', 'News'), ('AR', 'Article')], max_length=2),
        ),
    ]
