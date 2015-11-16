# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Ingredient, IngredientVariation, Recipe


admin.site.register(Ingredient)
admin.site.register(IngredientVariation)
admin.site.register(Recipe)
