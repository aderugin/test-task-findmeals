# -*- coding: utf-8 -*-
from django.db import models


class TitleMixin(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, db_index=True)

    class Meta:
        ordering = ['title']
        abstract = True

    def __str__(self):
        return self.title


class Ingredient(TitleMixin):
    pass


class IngredientVariation(TitleMixin):
    ingredient = models.ForeignKey(Ingredient)


class Recipe(TitleMixin):
    text = models.TextField(verbose_name='Текст рецепта')
    ingredients = models.ManyToManyField(IngredientVariation, verbose_name='Ингредиенты')
