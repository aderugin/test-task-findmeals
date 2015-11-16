# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from findmeals.base.views import IndexView


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^ajax/search/$', 'findmeals.base.views.ajax_search_view', name='search'),
    url(r'^ajax/ingredient_autocomplete/$', 'findmeals.base.views.ajax_autocomplete_view',
        name='ingredient-autocomplete')
]
