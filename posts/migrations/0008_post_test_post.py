# Generated by Django 3.0.5 on 2020-04-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_post_from_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='test_post',
            field=models.BooleanField(default=False),
        ),
    ]
