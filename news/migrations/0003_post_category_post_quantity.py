# Generated by Django 4.1.4 on 2022-12-12 15:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='news.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]