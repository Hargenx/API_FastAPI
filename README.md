# FastAPI OpenAI Description Generator

Este projeto utiliza o FastAPI para criar endpoints que gerenciam pedidos e geram descrições de produtos usando o modelo GPT-3.5 da OpenAI.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/Hargenx/fastapi-openai.git
    ```

2. **Navegue até o diretório do projeto:**

    ```bash
    cd fastapi-openai
    ```

3. **Instale as dependências usando pip:**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. **Execute o servidor FastAPI:**

    ```bash
    uvicorn main:app --reload
    ```

2. **Acesse a documentação Swagger visitando** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) **no seu navegador.**

## Endpoints

### `POST /ordens`

Cria um pedido com um produto específico e quantidade.

Exemplo de Requisição:

```json
{
    "produto": "laptop",
    "unidade": 1
}
```

### `POST /ordens_pydantic`

Cria um pedido utilizando o modelo Pydantic Ordem.

Exemplo de Requisição:

```json
{
    "produto": "tablet",
    "unidade": 2
}
```

### `POST /produto_descricao`
Gera uma descrição de produto usando o modelo GPT-3.5 da OpenAI.

Exemplo de Requisição:

```json
{
    "nome": "Smartphone",
    "nota": "Smartphone de alta performance com bateria de longa duração."
}
```

## Variáveis de Ambiente

- OPENAI_API_KEY: Chave de API necessária para acessar os serviços da OpenAI.
