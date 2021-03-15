from django.urls import path

from .views import HelloWorldPrinter

urlpatterns = [
    path('hello/', HelloWorldPrinter.as_view()),

]
