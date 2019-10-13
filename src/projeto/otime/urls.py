from django.urls import path
from .views import  index, salas, reservarHorario, professores, disciplinas, lista_professores, atualizar_professor, deletar_professor, criar_professor
urlpatterns = [
    path("", index, name = "index"),
    path("salas", salas, name = "salas"),
    path("reservarHorario", reservarHorario, name = "reservarHorario"),
    path("professores", professores, name = "professores"),
    path("disciplinas", disciplinas, name = "disciplinas"),
    path('listar_professores', lista_professores, name='lista_professores'),
    path('update/<int:id>/', atualizar_professor, name='atualizar_professor'),
  	path('delete/<int:id>/', deletar_professor, name='deletar_professor'),
   	path('new', criar_professor, name='criar_professores'),
]
