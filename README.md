# O'Time

``
O O'Time é uma aplicação web que auxilia na montagem de horários escolares de maneira simples e rápida.
``

## Início

Estas instruções permitem que você obtenha uma cópia do projeto e configure
em seu computador para desenvolvimento e testes.

### Pré-requisitos

Para baixar, compilar e executar em seu computador, você deve ter:

- Sistema de controle de versões `git` ([https://www.git-scm.com/])
- Kit de Desenvolvimento `python` ([https://www.python.org/])
- Framework para aplicações web `django` ([https://www.djangoproject.com/])

### Instalação

##### Ubuntu Linux

**Importante**: É aconselhável fazer um _update_ do `apt-get`:

```sh
sudo apt-get update
```

- git

```sh
sudo apt-get install git
```

- python

```sh
sudo apt-get install python3
```

**Importante**: caso não esteja instalado, instalar o `pip`, que é o software que usamos para instalar o Django

```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

Caso já esteja instalado, é aconselhável fazer um _upgrade_:

```sh
python -m pip install --upgrade pip
```

- django 

```sh
pip install Django
```

### Clonar o repositório

Para realizar um clone do projeto, execute:

```sh
git clone https://gitlab.devops.ifrn.edu.br/tads.cnat/pdsweb/2019.2/g-horarios.git
cd g-horarios
```

O clone do git cria um diretório chamado `g-horarios` se não for informado um
nome de diretório.

### Executar em modo desenvolvimento

Para executar em modo de desenvolvimento,
no diretório do projeto, digite:

```sh
python manage.py runserver
```

## Documentação

Verifique o diretório [`doc`](./doc/) para a documentação do sistema

## Contribuindo

Veja o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para maiores detalhes.

## Equipe de desenvolvimento

* **Eduardo Riev da Silva Oliveira** - *eduardoriev12@gmail.com*

* **Luan da Costa Redmann** - **

* **Rafael Horacio Soares de Abreu** - **

* **Rodrigo Pereira da Silva** - *missidia@hotmail.com*

* **Wallase Alan Costa de Morais** - *wallacealanmorais@gmail.com*

## Licença

Este projeto é licenciado pela GNU [GPL 3](LICENSE.md).
