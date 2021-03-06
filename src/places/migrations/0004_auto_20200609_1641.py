# Generated by Django 3.0.7 on 2020-06-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_placeimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=models.TextField(blank=True, null=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(max_length=200, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='sort_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Позиция'),
        ),
    ]
