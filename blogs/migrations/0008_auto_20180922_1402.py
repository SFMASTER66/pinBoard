# Generated by Django 2.1.1 on 2018-09-22 14:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0007_commenttvote_postvote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommenttVote',
            new_name='CommentVote',
        ),
    ]
