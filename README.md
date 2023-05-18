# Documentação do Web App de Busca de Produtos #

O Web App de Busca de Produtos é uma aplicação Flask que permite aos usuários fazerem buscas por produtos na plataforma Mercado Livre. Abaixo você encontrará informações sobre como usar e interagir com o Web App.


*Requisitos*

Certifique-se de ter os seguintes requisitos antes de executar o Web App:

requests: Biblioteca para enviar solicitações HTTP.
beautifulsoup4: Biblioteca para analisar e extrair dados de HTML e XML.
Flask: Framework web para criar aplicativos web em Python.

Você pode instalá-los usando o comando pip install -r requirements.txt no diretório do projeto.


*Executando o Web App*

Faça o download do código fonte do Web App em sua máquina.

Abra o terminal ou prompt de comando e navegue até o diretório onde o código fonte está localizado.

Execute o comando a seguir para iniciar o Web App: python app.py

O Web App será iniciado e estará acessível localmente no endereço http://127.0.0.1:5000/.

Após abrir o endereço acima, será direcionado para a página de login, que pode acessar usando as credenciais:
`Usuário: guest`
`Senha: 1234`

Depois, basta fazer sua busca na barra de busca e aguardar os resultados serem mostrados.


*Páginas do Web App:*

- Página de Login
    URL: /login
    Descrição: Página de login onde os usuários devem inserir suas credenciais de acesso.
    Métodos suportados: GET, POST

- Autenticação de Usuário
    URL: /autenticar
    Descrição: Rota responsável por autenticar os dados de acesso do usuário e redirecioná-lo para a página de busca em caso de sucesso.
    Métodos suportados: POST

- Página de Busca
    URL: /search
    Descrição: Página de busca onde os usuários podem pesquisar por produtos no Mercado Livre.
    Métodos suportados: GET, POST

- Rota de Busca
    URL: /search
    Descrição: Rota responsável por realizar a busca de produtos no Mercado Livre com base na query fornecida pelo usuário.
    Métodos suportados: POST


*Parâmetros:*

query: String contendo o termo de busca.
Retorno: JSON contendo os resultados da busca.
Funcionalidades Adicionais

Além das funcionalidades básicas de login e busca, o projeto possui um recusro adicional no arquivo `gerador_json.py`, que gera um arquivo em JSON, nomeado "resultado_pesquisa.json".
O arquivo `gerador_json.py` está todo comentado para uso e toda nova busca irá sobrescrever a busca anterior no arquivo "resultado_pesquisa.json".


*Considerações Finais*

O Web App de Busca de Produtos é uma aplicação simples que permite aos usuários pesquisar produtos no Mercado Livre. Você pode expandir e personalizar o aplicativo de acordo com suas necessidades adicionando recursos adicionais, como autenticação de usuário, armazenamento de resultados de busca e muito mais.

Sinta-se à vontade para explorar e adaptar o código-fonte do Web App para atender às suas necessidades específicas. Divirta-se!