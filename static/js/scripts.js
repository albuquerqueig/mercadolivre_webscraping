function importarDados() {
    fetch('resultado_pesquisa.json') // faz a leitura do arquivo JSON
        .then(response => response.json())
        .then(data => {
            let tabela = document.getElementById("tabelaDados").getElementsByTagName('tbody')[0]; // seleciona o corpo da tabela
            tabela.innerHTML = ""; // limpa a tabela antes de preencher com os novos dados

            // loop pelos dados do arquivo JSON e adiciona-os à tabela
            Object.keys(data).forEach(function(key) {
                let row = tabela.insertRow();
                let cell1 = row.insertCell(0);
                let cell2 = row.insertCell(1);
                cell1.innerHTML = data[key].title;
                cell2.innerHTML = data[key].price;
            });
        });
}