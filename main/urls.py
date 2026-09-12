from django.urls import path
from main.views import show_main, show_experience
from main.views import more_about_me

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('more/', more_about_me, name='more_about_me'),
]