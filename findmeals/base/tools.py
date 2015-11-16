# -*- coding: utf-8 -*-
from random import randint
from django.db import transaction
from .models import Recipe, Ingredient, IngredientVariation


def generate_content():
    # Генерация ингредиентов
    with transaction.atomic():
        print('Генерация ингредиентов')
        counter = 0
        while counter <= 1000:
            Ingredient.objects.create(title='Ингредиент %s' % counter)
            counter += 1
            print(counter)

    # Генерация вариаций ингредиентов
    with transaction.atomic():
        print('Генерация вариаций ингредиентов')
        for item in Ingredient.objects.all():
            for i in range(randint(3, 8)):
                IngredientVariation.objects.create(
                    ingredient=item,
                    title='Вариация %s, %s' % (i, item.title)
                )
            print(item.title)

    # Генерация рецептов
    with transaction.atomic():
        print('Генерация рецептов')
        counter = 0
        ingredients_ids = list(IngredientVariation.objects.values_list('id', flat=True))
        count = len(ingredients_ids)
        while counter <= 10000:
            obj = Recipe.objects.create(title='Рецепт %s' % counter, text='Текст рецепта %s' % counter)
            obj.ingredients.add(*[ingredients_ids[randint(1, count-1)]
                                for i in range(3, randint(4, 8))])
            counter += 1
            print(counter)
