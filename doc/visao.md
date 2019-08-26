# Documento de visão
# O'Time
## Introdução
### Resumo

`O O'Time é uma aplicação web que permite a gestão e montagem de horários de forma eficiente e simples.`

### Escopo

Principais responsabilidades e não responsabilidades do sistema.

### Responsabilidades

- Permitir que os usuários se cadastrem no sistema e tenham níveis de acesso diferentes de acordo com as preferências de um usuário principal.
- Permitir que os professores cadastrados possam enviar suas preferências de horário para a comissão de horários escolares.
- Notificar professores de eventuais mudanças no horário escolar.
- Garantir que não haja inconsistência nos dados.

### Não-responsabilidades

- Garantir acesso total no caso de perda de conexão com a internet.
- Permitir que os funcionários da escola conversem entre si.
- Segurança em caso de vazamento de senhas oriundo de descuido dos usuários.

### Diagrama Geral de Casos de uso

![](img/CDU.PNG)

### Casos de Uso

| Cod. | Caso de Uso | Descrição | Classificação |
| ---- | ----------- | --------- | ------------- |
| UC01 | Cadastrar tabelas de horário |	O gestor loga no sistema e seleciona a opção 'cadastrar tabelas'. Abre-se então as tabelas. | Primário |
| UC02 | Alterar tabela de horários| O gestor loga no sistema e escole alterar a tabela X. Abre-se então a tabela e ele pode editar clicando nas células. | Primário |
| UC03 | Deletar tabela de horários | O gestor loga no sistema e escole deletar a tabela X. Abre-se então uma mensagem de confirmação. | Secundário |
| UC04 | Visualizar tabelas cadastradas | O gestor loga no sistema e seleciona a opção 'visualizar tabelas cadastradas'. O sistema retorna uma tela com as tabelas cadastradas por aquele gestor. | Secundário |
| UC05 | Cadastrar horários de preferência | O professor loga no sistema e seleciona a opção 'cadastrar horários de preferência'. Abre-se então a tabela e ele pode editar clicando nas células. | Secundário |
| UC06 | Alterar horários de preferência | O professor loga no sistema e seleciona a opção 'alterar horários de preferência'. Abre-se então a tabela e ele pode editar clicando nas células. | Secundário |
| UC07 | Deletar horários de preferência | O professor loga no sistema e seleciona a opção 'deletar horários de preferência'. Abre-se então a tabela e ele pode editar clicando nas células. | Secundário |
| UC08 | Visualizar horários | O professor loga no sistema e seleciona a opção 'visualizar horários'. O sistema retorna uma tela com os horários cadastrados daquele professor. | Secundário |
| UC09 | Solicitar mudança de horário | O professor loga no sistema e seleciona a opção 'solicitar mudança de horário'. Abre-se então a tabela e ele seleciona a célula que deseja mudança. | Secundário |

### Atores

| Ator | Descrição |
| -------- | -------- |
| Gestor | Responsável pela criação de tabelas de horários e mudanças nas mesmas, se necessário. | 
| Professor | Podem visualizar as tabelas de horários, solicitar mudanças aos gestores e selecionar horários de sua preferência. |

## Clientes

```sh
O público-alvo do nosso sistema é formado principalmente por pessoas de instituições públicas,
que desejam adquirir um sistema que possibilite a gestão de horários de forma eficiente e simples.
```


## Requisitos

### Requisitos Funcionais

| Cod | Nome | Descrição | Categoria |
| --- | ---- | --------- | --------- |
| F01 | Cadastro de usuários | O sistema deve permitir que os usuários se cadastrem no mesmo. | Evidente |
| F02 | Login |	O sistema deve permitir que os usuários entrem no sistema usando suas credenciais. | Evidente |
| F03 | Recuperação de senha |	O sistema deve permitir que os usuários recuperem suas senhas, se necessário. | Evidente |
| F04 | Cadastro de horários | O sistema deve permitir que gestores cadastrem tabelas de horários. | Evidente |
| F05 | Alteração de horários | O sistema deve permitir que gestores alterem tabelas de horários. | Evidente |
| F06 | Deletar tabela de horários | O sistema deve permitir que gestores deletem tabelas de horários.  | Evidente |
| F07 | Notificação de mudanças de horário | O sistema deve notificar aos usuários de mudanças de horários. | Evidente |
| F08 | Cadastro de horários de preferência | O sistema deve permitir o cadastro de horários de preferência já cadastrados dos professores. | Evidente |
| F09 | Alteração de horários de preferência | O sistema deve permitir a alteração de horários de preferência dos professores. | Evidente |
| F09 | Remoção de horários de preferência | O sistema deve permitir a remoção de horários de preferência já cadastrados dos professores. | Evidente |
| F11 | Visualização de horários | O sistema deve permitir aos usuários que visualizem os horários cadastrados pelos gestores. | Evidente |
| F12 | Solicitação de mudanças de horários | O sistema deve permitir aos professores solicitarem aos gestores mudanças de horários já cadastrados. | Evidente |


### Requisitos não funcionais

| Cód. | Nome | Descrição | Categoria | Obrigatoriedade | Permanência |
| ---- | ---- | --------- | --------- | --------------- | ----------- |
| NF01 | Interface Web | Deve funcionar em uma plataforma web | Interface | Obrigatório | Permanente |
| NF02 | Interface Mobile |	Deve funcionar em uma plataforma mobile | Interface | Desejável | Transitório |
| NF03 | Tecnologias de Desenvolvimento | Será desenvolvido usando o Django Framework na linguagem Python e HTML5 / JavaScript / CSS. | Implementação | Obrigatório | Transitório |
| NF04 | Restrição de horários | Permitir que apenas gestores modifiquem os horários | Implementação | Obrigatório | Transitório |
| NF05 | Exportação do arquivo de horários | O sistema deve permitir aos usuários exportar o arquivo de horários para outros formatos. | Especificação | Desejável | Transitório |
