# Ambiente de Desenvolvimento

## Instalação

### Arquivos de instalação do MySQL

Arquivos necessários para a instalação do MySQL:

 - [MySQL Installer 8.0.34](https://dev.mysql.com/downloads/installer/)
 - [MySQL Workbench 8.0.34](https://dev.mysql.com/downloads/workbench/)

### Instalando o MySQL Installer

Para instalar o MySQL Installer e Workbench, siga os seguintes passos indicados nas imagens:

<img src="img/mysql/installer/part1.png" width="800"/>
<img src="img/mysql/installer/part2.png" width="800"/>
<img src="img/mysql/installer/part3.png" width="800"/>
<img src="img/mysql/installer/part4.png" width="800"/>
<img src="img/mysql/installer/part5.png" width="800"/>
<img src="img/mysql/installer/part6.png" width="800"/>
<img src="img/mysql/installer/part7.png" width="800"/>
<img src="img/mysql/installer/part8.png" width="800"/>
<img src="img/mysql/installer/part9.png" width="800"/>
<img src="img/mysql/installer/part10.png" width="800"/>
<img src="img/mysql/installer/part11.png" width="800"/>
<img src="img/mysql/installer/part12.png" width="800"/>
<img src="img/mysql/installer/part13.png" width="800"/>
<img src="img/mysql/installer/part14.png" width="800"/>
<img src="img/mysql/installer/part15.png" width="800"/>


### Configurando o MySQL Workbench

Para configurar o MySQL Workbench, siga os seguintes passos:

<img src="img/mysql/workbench/part1.png" width="800"/>
<img src="img/mysql/workbench/conn1.png" width="800"/>
<img src="img/mysql/workbench/conn2.png" width="800"/>
<img src="img/mysql/workbench/conn3.png" width="800"/>

### Criando a Database

Para criar a Database, siga os seguintes passos:

<img src="img/mysql/workbench/conn4.png" width="800"/>

### Python 

Linux:
``` 
sudo apt install python3.11
```

Para Windows:

- [Instalador .exe versão 3.11.0](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)

Execute o arquivo executável e siga os passos:

<img src="img/python/python_install_part1.png" width="800"/>
<img src="img/python/python_install_part2.png" width="800"/>
<img src="img/python/python_install_part3.png" width="800"/>
<img src="img/python/python_install_part4.png" width="800"/>

Após seguir os passos acima, abra um terminal e execute o seguinte comando para verificar se o Python foi instalado:

``` 
python --version
```

## Configuração

### Baixar API

Acesse o [repositório](https://github.com/V-Perotto/AxyaTest_API/) e baixe via HTTPS ou via Zip.

- HTTPS: https://github.com/V-Perotto/AxyaTest_API.git

O diretório da API consiste nesse modelo:

```
- AxyaTest_API/
    - controllers/
    - models/
    - tests/
    - app.py
    - config.py
    - requirements.txt
```

### Criar Virtualenv

Após verificada a instalação do Python, baixe o <code>virtualenv</code>

```
pip install virtualenv
``` 

Acesse o diretório da API, abra um terminal e crie um ambiente virtual usando o seguinte comando: 

```
venv api
```

O diretório pode ficar separado do diretório do ambiente virtual, como no exemplo abaixo:

```
- api/ (ambiente virtual)
- AxyaTest_API/
    - controllers/
    - models/
    - tests/
    - app.py
    - config.py
    - requirements.txt
```

### Ativar Virtualenv

Ainda no mesmo diretório e terminal acesse o diretório do ambiente virtual e ative-o com o seguinte comando:

- No terminal do Git Bash ou Linux:
```
source api/Scripts/activate
```

- No Windows: 
```
cd api/Scripts/
activate
```

Ao ativar o ambiente virtual, ele deverá ficar parecido com a seguinte imagem, indicando que está ativo.

<img src="img/python/venv.png" width="400"/>

### Baixar as bibliotecas

**IMPORTANTE**: Para baixar as bibliotecas e requisitos necessários para rodar, você deverá estar com o ambiente virtual ativo.

Instale as bibliotecas usando o seguinte comando:

```
python pip install -r requirements.txt
```

Todas as bibliotecas e respectivas versões estão indicadas no arquivo <code>requirements.txt</code>.

## Inicialização

Para poder inicializar ambos API e testes, será necessário abrir um terminal para cada e rodar os seguintes comandos:

### Ativar a API

Primeiro altere as seguintes variáveis no arquivo <code>app.py</code>.

Variáveis:

- <code>(str) host</code>: host da aplicação. Ex.: "localhost"
- <code>(int) port</code>: porta da aplicação. Ex.: 3306
- <code>(str) user</code>: usuário do banco de dados. Ex.: "root"
- <code>(str) pwd</code>: senha do usuário do banco de dados.
- <code>(str) db</code>: database criada no banco de dados. 

```
app = create_app(<host>, <port>, <user>, <pwd>, <db>)
```

Após inserir os seguintes dados, execute a linha de comando abaixo em um terminal separado.

```
python app.py 
```

## Rodar os Testes

### Usando TDD com RobotFramework

Para rodar os testes, acesse o diretório <code>TDD/</code> em um terminal separado.

**IMPORTANTE**: A API deverá estar ativa para os testes funcionarem.

Para rodar os testes via terminal, use:

```
robot test.robot
```

Seu retorno deverá ser igual a imagem abaixo: 

<img src="img/robot/log.png" width="600"/>

Para mais informações do _log_ detalhado do <code>RobotFramework</code>, acesse o **Log** no seu navegador.

Ele deverá ser semelhante à imagem abaixo:

<img src="img/robot/output.png" width="800"/>

### Usando Python

Para rodar os testes, acesse o diretório <code>tests/</code> em um terminal separado.

**IMPORTANTE**: A API deverá estar ativa para os testes funcionarem.

Como utilizar os testes via terminal:

Variáveis:

- <code>[método]</code>: será a opção que você testará na API. Ex.: <code>create</code>

- <code>[*argumentos]</code>: será os argumentos desse método que você irá passar. Alguns métodos exigem diferentes tipos e quantidade de dados para poderem ser executados.

Argumentos disponíveis:

- <code>create [nome] [sobrenome] [email] [telefone]</code>

- <code>read [id]</code>

- ¹<code>update [id]</code> <code>[nome]</code> e/ou <code>[sobrenome]</code> e/ou <code>[email]</code> e/ou <code>[telefone]</code>

- <code>delete [id]</code>

- <code>search [nome]</code>

¹*No caso de <code>update</code>, você poderá passar somente 1 valor, desde que utilize <code>.</code> para indicar que não deseja passar o respectivo valor (**mesmo assim, deverá seguir a ordem**).*

Utilize o teste com o seguinte comando:

```
python test.py [método] [*argumentos]
```