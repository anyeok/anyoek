# Generated by Django 4.0.3 on 2024-07-18 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='content',
            new_name='content2',
        ),
    ]