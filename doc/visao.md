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
