# Generated by Django 4.1.4 on 2022-12-17 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_alter_post_post_text_alter_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.author', verbose_name='Автор поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_rating',
            field=models.IntegerField(default=0, verbose_name='Рейтинг поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(verbose_name='Текст поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=90, verbose_name='Заголовок поста'),
        ),
    ]
