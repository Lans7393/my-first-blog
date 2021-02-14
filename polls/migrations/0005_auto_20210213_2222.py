# Generated by Django 2.2.17 on 2021-02-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210210_0129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'вариант ответа', 'verbose_name_plural': 'варианты ответа'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': 'вопросы'},
        ),
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(max_length=200, verbose_name='вариант ответа'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='количество голосов'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=200, verbose_name='вопрос'),
        ),
    ]
