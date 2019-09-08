### Caso de Uso: Editar turma.
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: Deseja editar informações da turma.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O ator segue o fluxo do CDU "Listar turmas" e seleciona a turma no qual deseja alterar os slots de horários.
2. O sistema redireciona o ator para uma página contendo as informações da turma e um menu de opções de edição.
3. O ator seleciona a opção "Editar turma" no menu de opções da turma.
4. O sistema solicita que o ator selecione a operação que deseja realizar.
5. O ator seleciona a opção "Alterar informações da turma".
6. O sistema redireciona o ator para uma página contendo as informações cadastradas naquela turma.
7. O ator faz as alterações necessárias e seleciona a opção "Confirmar alterações".
8. O sistema exibe uma mensagem de sucesso informando que as alterações foram realizadas.
9. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**5a. O ator seleciona a opção "Deletar turma"**

6. O sistema solicita que o ator confirme que deseja excluir aquela turma.
7. O ator seleciona a opção "Confirmar".
8. O sistema exibe uma mensagem de sucesso informando que a turma selecionada foi deletada.
9. CDU finalizado.

**7a. O ator preenche algum dado incorreto**

8. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
9. O ator preenche novamente os dados incorretos e seleciona a opção "Confirmar".
10. Volta ao passo 8 do fluxo principal.

**7b. O ator não preenche algum dado**

8. O sistema retorna uma mensagem de erro, informando quais dados ainda precisam ser preenchidos.
9. O ator preenche os dados que faltam e seleciona a opção "Confirmar".
10. Volta ao passo 8 do fluxo principal.