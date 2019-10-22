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

1. O gestor clica no botão novo na pagina de disciplina.
2. O sistema redireciona para a pagina com formulário para cadastro de disciplina, contendo os  campos para **código**, **nome** e **carga horária total**.
3. O gestor preenche o formulario e clica no botão salvar.
4. O sistema redireciona para a pagina de diciplina.
5. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

3. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
4. Volta ao passo 4 do fluxo principal.