# Desafio Semifinal How Bootcamps em parceria com Stone

## Participante Marcelo Lopes Valerio

### e-mail: mar.valerio@hotmail.com.br

## Instruções para rodar o codigo

### O primeiro passo é, caso não tenha criado, criar um ambiente virtual para instalar os pacotes
### Os comandos para criar e ativar no windows são:

    python3 -m venv .venv 
    .venv\Scripts\activate.bat

### Linux:

    python3 -m venv .venv 
    source .venv/bin/activate

### Com isso feito, é preciso instalar os recursos e pacotes utilizados, localizados no arquivo requirements.txt:

    pip install -r requirements.txt

### Depois disso, renomeie o arquivo exemplo_dados.txt para .env,e coloque lá os seus dados do banco de dados

### Por ultimo, crie um super user, para rodar o codigo, por exemplo, no postman, e possuir as autorizações na API

    ./manege.py createsuperuser

## Com isso, a parte de python está pronta, agora sobre o banco de dados MySQL:

### Crie o banco de dados, no MySQL com o mesmo nome colocado na pasta .env em NAME:

    CREATE schema Coloque o nome aqui

### agora rode os dois comandos abaixo para migrar as tabelas para o banco:

    ./manage.py makemigrations banco_digital
    ./manage.py migrate

### Pronto, agora é só dar o comando abaixo para iniciar a aplicação:

    ./manage.py runserver

### OBS: Para ter acesso aos dados, é preciso que voce entre com seu super user, na direita, parte superior da tela
###
### Para rodar os testes, deve criar, na interface de executar e depurar, e adicionar a configuração do Django test
### OBS2: Para rodar os testes é necessário comentar a linha 'permission_classes = (IsAuthenticated,)' em todas as views, caso contrário, falharão. Além disso, é necessário que o debug seja setado para Django test, e então ativá-lo para rodar os testes.

# Sobre o Desafio

## Criação de um banco digital com Django

### Funcionalidades:
###
### Criar/Deletar/Alterar/Buscar um usuário -> URL: http://127.0.0.1:8000/usuario/ e http://127.0.0.1:8000/usuario/id_usuario/
###
### Consulta de todas as contas criadas -> URL: http://127.0.0.1:8000/usuario/
###
### Consulta da saldo de uma conta -> URL: http://127.0.0.1:8000/usuario/cod_conta_usuario/saldo/
###
### Transferir entre duas contas criadas -> URL: http://127.0.0.1:8000/transferencias/
###
### Consultar as tranferencias recebidas/enviadas por uma conta -> URL: http://127.0.0.1:8000/transferencias/cod_conta_usuario/recebidas/ ou http://127.0.0.1:8000/transferencias/cod_conta_usuario/enviadas/