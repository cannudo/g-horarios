### Caso de Uso: Reservar horário(s)
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: deseja reservar horário(s).

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.
- Haver, no minimo, um professor, uma disciplina e uma sala de aula cadastrada no sistema.
 
**Pós-condições**
- Horario(s) foi(foram) reservado(s) no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor indica que quer reservar horários.
2. O sistema abre o formulário para reserva de horários, contendo listas de **professores**, de **salas de aula** e de **disciplinas**.
3. O gestor seleciona um de cada opção.
4. O sistema torna clicável, na tabela, os horários que estão disponíveis para a sala selecionada. Além disso, exibe um contador de aulas restantes ao cadastro, baseado na carga horária total da disciplina.
5. O gestor clica no(s) horário(s) que deseja reservar.
6. O sistema torna clicável o botão para confirmar a ocupação quando ele seleciona a quantidade de horários igual aos créditos da disciplina.
7. O gestor clica em "confirmar reserva".
8. O sistema cadastra a reserva e CDU finaliza.

**Fluxos alternativos ou excepcionais**