# Generated by Django 2.2.17 on 2021-02-09 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210210_0121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choiсe_text',
            new_name='choice_text',
        ),
    ]