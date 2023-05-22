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
                let cell3 = row.insertCell(2);
                let cell4 = row.insertCell(3);
                let cell5 = row.insertCell(4);
                let cell6 = row.insertCell(5);
                
                cell1.innerHTML = data[key].title;
                cell2.innerHTML = data[key].price;
                cell3.innerHTML = data[key].sold_by;
                cell4.innerHTML = data[key].discount;
                cell5.innerHTML = data[key].installments;
                cell6.innerHTML = data[key].shipping;
            });
        });
}