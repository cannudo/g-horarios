### Caso de Uso: Cadastrar sala de aula
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: deseja cadastrar sala de aula.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Pós-condições**
- Uma sala de aula é cadastrada no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor indica que quer cadastrar uma sala de aula.
2. O sistema abre o formulário para cadastro de sala de aula, contendo os campos para **nome**, **número**, **capacidade** e **tipo**.
3. O gestor preenche.
4. O sistema torna clicável o botão para confirmar o cadastro.
5. O gestor clica no botão para confirmar.
6. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

4. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
5. Volta ao passo 4 do fluxo principal.

**3b. O ator não preenche algum dado**

4. O sistema retorna uma mensagem de erro, informando quais dados ainda precisam ser preenchidos.
5. Volta ao passo 4 do fluxo principal.

**3c. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 5 do fluxo principal.