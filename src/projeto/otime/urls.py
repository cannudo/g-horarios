from django.urls import path
from .views import  index, salas, reservarHorario, professores, disciplinas, atualizar_professor, deletar_professor, atualizar_disciplina, atualizar_sala, deletar_disciplina, deletar_sala
urlpatterns = [
    path("", index, name = "index"),
    path("salas", salas, name = "salas"),
    path("reservarHorario", reservarHorario, name = "reservarHorario"),
    path("professores", professores, name = "professores"),
    path("disciplinas", disciplinas, name = "disciplinas"),
    path('update/professor/<int:id>/', atualizar_professor, name='atualizar_professor'),
  	path('professores/<int:id>/', deletar_professor, name='deletar_professor'),
    path('update/disciplina/<int:id>/', atualizar_disciplina, name='atualizar_disciplina'),
    path('update/sala/<int:id>/', atualizar_sala, name='atualizar_sala'),
  	path('delete/disciplina/<int:id>/', deletar_disciplina, name='deletar_disciplina'),
    path('delete/sala/<int:id>/', deletar_sala, name='deletar_sala'),
]
