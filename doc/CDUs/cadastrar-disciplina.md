### Caso de Uso: Cadastrar disciplina
---
**Ator principal:** Gestor.

**Interessados e Interesses:**
- Gestor: deseja cadastrar disciplinas.

**Pré-Condições:**
- Ter cadastro completo, estar logado no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor indica que quer cadastrar uma disciplina.
2. O sistema abre o formulário para cadastro de disciplina, contendo os  campos para **código**, **nome** e **carga horária total**.
3. O gestor preenche.
4. O sistema torna clicável o botão para confirmar o cadastro.
5. O gestor clica no botão para confirmar.
6. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

3. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
4. Volta ao passo 4 do fluxo principal.

**3b. A conexão com a internet cai**

4. O sistema exibe um alerta informando que não há conexão com a internet.
5. O gestor volta ao passo 5 do fluxo principal.

**3c. O gestor tenta cadastrar um número de créditos semanais superior ao número de créditos totais ou ao número de slots semanais**

3. O sistema exibe um erro acima do campo de quantidade de créditos semanais e solicita correção.
4. O gestor volta ao passo 3 do fluxo principal.