rom django.urls import path
from . import views

app_name = "otime"
urlpatterns = [
    path("", views.index, name = "index"),
    path("reservarHorario", views.reservarHorario, name = "reservarHorario")
]
