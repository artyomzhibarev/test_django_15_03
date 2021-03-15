from django.shortcuts import render

from django.views import View
from django.http import HttpResponse


class HelloWorldPrinter(View):
    def get(self, request):
        html = """<h1>Hello, World</h1>"""
        return HttpResponse(html)
