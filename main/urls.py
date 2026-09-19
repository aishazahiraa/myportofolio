from django.urls import path
from main.views import show_main, show_experience
from main.views import more_about_me
from main.views import create_experience, create_education, update_education, delete_education
from main.views import show_json, show_json_by_id, show_xml, show_xml_by_id

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('more/', more_about_me, name='more_about_me'),
    path("experience/add/", create_experience, name="create_experience"),
    path("education/add/", create_education, name="create_education"),
    path("education/<int:id>/edit/", update_education, name="update_education"),
    path("education/<int:id>/delete/", delete_education, name="delete_education"),
    path("json/", show_json, name="show_json"),
    path("json/<uuid:id>/", show_json_by_id, name="show_json_by_id"),
    path("xml/", show_xml, name="show_xml"),
    path("xml/<uuid:id>/", show_xml_by_id, name="show_xml_by_id"),
]