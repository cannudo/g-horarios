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

1. O gestor clica na opção "Professores" do menu e em seguida seleciona o botão **Novo**. 
2. O sistema abre o formulário para cadastro de um professor, contendo os campos para **nome**, **telefone**, **email** e **matrícula**.
3. O gestor preenche todos os campos e clica no botão ***Salvar***.
4. O sistema exibe uma mensagem de confirmação do cadastramento.
5. CDU finalizado.

**Fluxos alternativos ou excepcionais**

**3a. O ator preenche algum dado incorreto**

3. O sistema retorna uma mensagem de erro, informando quais dados precisam ser corrigidos.
4. Volta ao passo 3 do fluxo principal.

**3b. O professor já existe**

5. O sistema retorna uma mensagem de erro, informando que o professor já foi cadastrado no sistema.
6. Caso de uso é cancelado
