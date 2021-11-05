## CRUD Simples usando Flask e SQLAlchemy

### Como rodar esse projeto

```
$ python3 -m venv venv
```

```
$ source venv/bin/activate
```

```
$ pip install -r requirements.txt
```

Crie um arquivo .env na raíz do projeto com:

```
$ touch .env
```

e insira as seguintes informações (substituindo pelas suas configurações):
<small>Nota: este projeto usa MySQL 8 na porta padrão (3306)</small>

```
DB_USER=<SEU USUARIO>
DB_PASSWORD=<SUA SENHA> (caso não haja, deixe em branco)
DB_HOST=<HOST DO SEU BANCO>
DB_NAME=<NOME DO SEU BANCO>
```
