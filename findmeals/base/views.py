# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from .models import Recipe, Ingredient


class IndexView(TemplateView):
    template_name = 'search.html'


def ajax_search_view(request):
    context = {'recipes': []}

    if 'q' in request.GET:
        queryset = Recipe.objects.filter(title__icontains=request.GET['q'])\
            .prefetch_related('ingredients')

        if 'include' in request.GET:
            queryset = queryset.filter(
                ingredients__ingredient__id__in=request.GET['include'])

        if 'exclude' in request.GET:
            queryset = queryset.exclude(
                ingredients__ingredient__id__in=request.GET['exclude'])

        context['recipes'] = [{'title': recipe.title, 'ingredients':
                               [ingredient.title for ingredient in recipe.ingredients.all()]}
                              for recipe in queryset[:20]]

    return JsonResponse(context)


def ajax_autocomplete_view(request):
    if request.is_ajax():
        context = {'suggestions': []}
        if 'q' in request.GET:
            queryset = Ingredient.objects.filter(title__icontains=request.GET['q'])\
                .values_list('id', 'title')[:10]
            context['suggestions'] = [{'value': item[1], 'data': item[0]} for item in queryset]
        return JsonResponse(context)
    raise Http404
