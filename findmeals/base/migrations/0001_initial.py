# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Название', db_index=True, max_length=255)),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IngredientVariation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Название', db_index=True, max_length=255)),
                ('ingredient', models.ForeignKey(to='base.Ingredient')),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(verbose_name='Название', db_index=True, max_length=255)),
                ('text', models.TextField(verbose_name='Текст рецепта')),
                ('ingredients', models.ManyToManyField(verbose_name='Ингредиенты', to='base.IngredientVariation')),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
    ]
