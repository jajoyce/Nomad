# Generated by Django 4.0.2 on 2022-02-14 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_profile_options_comment_created_at_post_img_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created_at']},
        ),
    ]
