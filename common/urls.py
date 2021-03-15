from django.urls import path

from .views import RandomNumber, CurrentDateView

urlpatterns = [
    path('randomnumber/', RandomNumber.as_view()),
    path('datetime/', CurrentDateView.as_view())

]
