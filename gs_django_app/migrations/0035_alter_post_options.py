# Generated by Django 4.0.4 on 2022-04-17 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gs_django_app', '0034_postresponse_remove_post_likes_post_responses_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created_at',)},
        ),
    ]