# Ambiente de Desenvolvimento
## Instalação

### MySQL

Arquivos necessários para a instalação do MySQL:

 - [MySQL Installer 8.0.34](https://dev.mysql.com/downloads/installer/)
 - [MySQL Workbench 8.0.34](https://dev.mysql.com/downloads/workbench/)

### Python 

Para Windows:

- [Instalador .exe versão 3.11.0](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)

Linux:
``` 
sudo apt install python3.11
```

## Configuração
### Criar Virtualenv
```
venv api </code>
```

### Acessar Virtualenv
No terminal do Git Bash ou Linux:
```
source api/Scripts/activate
```

No Windows: 
```
cd api/Scripts/
activate
```

### Baixar as bibliotecas

Para baixar as bibliotecas e requisitos necessários para rodar 

```
python pip install -r requirements.txt
```

## Inicialização

Para poder inicializar ambos API e testes, será necessário abrir um terminal para cada e rodar os seguintes comandos:

### Ativar a API
```
python app.py 
```

### Rodar os Tests
```
python tests/test.py [método] [*argumentos]
```