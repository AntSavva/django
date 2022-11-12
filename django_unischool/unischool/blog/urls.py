from django.urls import path, re_path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("new/<int:catid>/", index_2),
    re_path(r"^arcvive/(?P<year>[0-9]{4})/", arcvive),
    path("create/", create),
    path("edit/<int:id>/", edit),
    path("delete/<int:id>/", delete),
]

