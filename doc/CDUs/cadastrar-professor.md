### Caso de Uso: Cadastrar professor
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: deseja cadastrar professor.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
- Um professor é cadastrado no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor indica que quer cadastrar um professor.
2. O sistema abre o formulário para cadastro de professor, contendo os  campos para **nome**, **telefone**, **e-mail** e **matrícula**.
3. O gestor preenche.
4. O sistema torna clicável o botão para confirmar o cadastro.
5. O gestor clica no botão para confirmar
6. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

3. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
4. Volta ao passo 4 do fluxo principal.

**3b. O professor já existe**

5. O sistema retorna uma mensagem de erro, informando que o professor já foi cadastrado no sistema.
6. CDU finalizado

**3c. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 5 do fluxo principal
