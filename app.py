import requests
from bs4 import BeautifulSoup
import json
from flask import Flask, request, render_template, session, flash, url_for, redirect

class Users:
    def __init__(self, nome, nickname, senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha

user1 = Users("Guest", "guest", "1234")
user2 = Users("Guest", "guest", "1234")
user3 = Users("Guest", "guest", "1234")

usuarios = {user1.nickname : user1,
            user2.nickname : user2,
            user3.nickname : user3}

app = Flask(__name__)
app.secret_key = '21052002'

@app.route('/')
def index():
    return render_template('login.html')

# Criar rota de Criar usuário

# Página de validação de dados de acesso
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

# Criando autenticação de dados de acesso
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado!')
            return redirect(url_for('search'))
    flash('Usuário ou senha inválidos!')
    return redirect(url_for('login'))

# Rota de busca do termo chave/query
@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'usuario_logado' not in session:
        return redirect(url_for('login', proxima=url_for('search')))
    if request.method == 'POST':
        query = request.form['query']
        url = "https://lista.mercadolivre.com.br/"
        search_url = url + query
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("li", class_="ui-search-layout__item")
        payload = {}
        for i, result in enumerate(results):
            title = result.find("h2", class_="ui-search-item__title").text.strip()
            price = result.find("span", class_="price-tag-fraction").text.strip()
            sold_by = result.find("p", class_="ui-search-official-store-label ui-search-item__group__element shops__items-group-details ui-search-color--GRAY")
            discount = result.find("span", class_="ui-search-price__discount")
            installments = result.find("div", class_="ui-search-installments ui-search-color--LIGHT_GRAY")
            shipping = result.find("span", class_="ui-search-item__shipping ui-search-color--LIGHT_GRAY")
            
            payload[i] = {
                "title": title,
                "price": "R$ " + price + ",00",
                "sold_by": sold_by.text.strip() if sold_by else "",
                "discount": discount.text.strip() if discount else "",
                "installments": installments.text.strip() if installments else "",
                "shipping": shipping.text.strip() if shipping else "Consulte o frete"
            }
        payload_json = json.dumps(payload)
        return payload_json
    else:
        return render_template('search.html')
    
    # Criar um CRUD ou apenas função de "Salvar resultados das buscas feitas e ver resultados das buscas feitas"

    # Criar uma rota para as funções acima

if __name__ == '__main__':
    app.run(debug=True)