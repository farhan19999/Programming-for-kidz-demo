# Generated by Django 4.1.7 on 2023-02-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='readingmaterial',
            name='contentTopic',
            field=models.CharField(default='For Loop', max_length=255),
            preserve_default=False,
        ),
    ]
