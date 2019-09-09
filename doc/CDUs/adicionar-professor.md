### Caso de Uso: Adicionar curso
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: deseja adicionar cursos à uma diretoria.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O ator seleciona a opção "Adicionar professor" na página "Visualizar professores cadastrados".
2. O sistema o redireciona a uma tela contendo as informações que ele deve preencher para cadastrar o professor.
3. O ator preenche as informações solicitadas e seleciona a opção "Confirmar".
4. O sistema exibe uma mensagem de sucesso, informando ao ator que o professor foi cadastrado com sucesso.
5. O sistema redireciona o ator para uma página contendo a lista de professores já cadastrados.
6. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

4. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
5. O ator preenche novamente os dados incorretos e seleciona a opção "Confirmar".
6. Volta ao passo 4 do fluxo principal.

**3b. O ator não preenche algum dado**

4. O sistema retorna uma mensagem de erro, informando quais dados ainda precisam ser preenchidos.
5. O ator preenche os dados que faltam e seleciona a opção "Confirmar".
6. Volta ao passo 4 do fluxo principal.

**3c. O professor já existe**

4. O sistema retorna uma mensagem de erro, informando que o professor já foi cadastrado no sistema.
7. CDU finalizado
