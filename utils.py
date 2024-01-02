from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
def get_api_key():
    return os.getenv("OPENAI_API_KEY")

cliente = OpenAI(api_key=get_api_key())


'''import json

def get_api_key():
    with open('./config.json') as config_file:
        config = json.load(config_file)
        return config['API_KEY']

cliente = OpenAI(api_key=get_api_key())'''

def gerar_descricao_produto(produto):
    try:
        prompt = (
            "Como um gerador de descrição de produto, gere uma descrição de produto em rich text de vários parágrafos com emojis a partir das informações fornecidas a você.\n"
            f"Nome do produto: {produto.nome}, nota: {produto.nota}\n"
        )

        response = cliente.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente prestativo."},
                {"role": "user", "content": prompt}
            ]
        )

        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)