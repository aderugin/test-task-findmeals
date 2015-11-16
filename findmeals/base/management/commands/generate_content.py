# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from findmeals.base.tools import generate_content


class Command(BaseCommand):
    help = 'Generate content for test'

    def handle(self, *args, **options):
        generate_content()
