# MS-Curriculos 
## Microserviço de gerenciamento de dados dos curriculos de candidatos da plataforma BAE Brasil

## 1. Instalação e Execução do Servidor Flask:
Importante: pressupõe-se o uso de gerenciadores de pacote e de ambientes virtuais como ```pip``` 
e ```venv```, respectivamente ou ```pipenv```.

### 1.1. Instalação das dependências:
```shell
pip install -r requirements.txt
```

### 1.2. Inicialização do banco de dados:
No diretório ```/src/api``` executar o comando:
```shell
flask init_db
```

### 1.3. Inicialização da aplicação:
No diretório ```/src/api``` executar o comando:
```shell
flask run
```

## 2. Endpoints Disponíveis:
### 2.1. Curriculos:

> **GET** <br>
> **Listar** todos os curriculos: ```/curriculos/list``` <br>
> **Buscar** por id_curriculo: ```/curriculos/get``` <br>

> **POST** <br>
> **Criar** novo: ```/curriculos/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_curriculo: ```/curriculos/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_curriculo: ```/curriculos/delete```

### 2.2. Formações:
> **GET** <br>
> **Listar** todas as formacoes de um curriculo por id_curriculo: ```/formacoes/list``` <br>
> **Buscar** por id_curriculo: ```/formacoes/get``` <br>

> **POST** <br>
> **Criar** novo: ```/formacoes/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_curriculo: ```/formacoes/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_curriculo: ```/formacoes/delete```

### 2.3. Experiências Profissionais:

> **GET** <br>
> **Listar** todas experiencias profissionais de um curriculo por id_curriculo: ```/experiencias_profissionais/list``` <br>
> **Buscar** por id_experiencia_profissional: ```/experiencias_profissionais/get``` <br>

> **POST** <br>
> **Criar** novo: ```/experiencias_profissionais/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_experiencia_profissional: ```/experiencias_profissionais/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_experiencia_profissional: ```/experiencias_profissionais/delete```
