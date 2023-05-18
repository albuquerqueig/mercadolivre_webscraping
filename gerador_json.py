import requests
from bs4 import BeautifulSoup
import json

# URL da página do Mercado Livre para realizar a pesquisa
url = "https://lista.mercadolivre.com.br/"

# Defina entre as aspas duplas o Termo de pesquisa/item
query = "processador intel i7"

# URL final para realizar a pesquisa
search_url = url + query

# Realiza a requisição HTTP para a página de resultados da pesquisa
response = requests.get(search_url)

# Analisa o HTML da página com a biblioteca BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Encontra todos os resultados da pesquisa na página
results = soup.find_all("li", class_="ui-search-layout__item")

# Cria um dicionário vazio para armazenar as informações dos resultados
payload = {}

# Para cada resultado, extrai as informações do título e do valor
for i, result in enumerate(results):
    title = result.find("h2", class_="ui-search-item__title").text.strip()
    price = result.find("span", class_="price-tag-fraction").text.strip()

    # Adiciona as informações do resultado ao dicionário de payload
    payload[i] = {
        "title": title,
        "price": price
    }

# Converte o dicionário de payload para JSON
payload_json = json.dumps(payload)

# Imprime o payload JSON resultante
print(payload_json)

# Cria um arquivo em JSON com as informações coletadas
with open("resultado_pesquisa.json", "w") as file:
    json.dump(payload, file)