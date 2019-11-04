### Caso de Uso: Cadastrar disciplina
---
**Ator principal:** 
- Gestor.

**Interessados e Interesses:**
- Gestor: deseja cadastrar disciplinas.

**Pré-Condições:**
- Ter clicado em lista diciplina.

**Pós-condições**
- Uma disciplina é cadastrado no sistema.

**Cenário de Sucesso Principal (ou Fluxo Básico):**

1. O gestor clica na opção "Disciplinas" do menu e em seguida seleciona o botão **Novo**. 
2. O sistema abre o formulário para cadastro de um professor, contendo os campos para **nome**, **código** e **carga_horária**.
3. O gestor preenche todos os campos e clica no botão **Salvar**.
4. O sistema exibe uma mensagem de confirmação do cadastramento.
5. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

3. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
4. Volta ao passo 3 do fluxo principal.

**3b. A conexão com a internet cai**

3. O sistema exibe um alerta informando que não há conexão com a internet.
4. O gestor volta ao passo 4 do fluxo principal.

**3c. O gestor tenta cadastrar um número de créditos semanais superior ao número de créditos totais ou ao número de slots semanais**

3. O sistema exibe um erro acima do campo de quantidade de créditos semanais e solicita correção.
4. O gestor volta ao passo 3 do fluxo principal.