from django.urls import pathfrom . import views

urlpatterns = [path("hello/", views.say_hello)]
