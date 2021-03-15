from django.shortcuts import render

from datetime import datetime
from random import randint

from django.views import View
from django.http import HttpResponse


class CurrentDateView(View):
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)


class RandomNumber(View):
    def get(self, request):
        html = f"""<h1>{randint(-100, 100)}</h1>"""
        return HttpResponse(html)
