import requests
import json


url = 'http://127.0.0.1:8000/ordens_pydantic'
headers = {
    'accept': 'application/json'
}
params = {
    'produto': 'laptop',
    'unidades': '1'
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(params))
    response.raise_for_status()  # Adicionando tratamento para erros HTTP
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Erro de fazer o HTTP request: {e}")
