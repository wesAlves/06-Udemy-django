# Generated by Django 4.1.1 on 2022-11-13 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='reivew_text',
            new_name='review_text',
        ),
    ]