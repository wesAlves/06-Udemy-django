# Generated by Django 4.1.1 on 2022-11-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('reivew_text', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]