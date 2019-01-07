# language: pt
Funcionalidade: Pesquisar no Google
    Realizar pesquisas no Google afim de garantir o retorno esperado da busca.

    Eu como usuário
    Quero realizar uma busca no Google
    Afim de obter o retorno que preciso

    Cenario: Realizar Pesquisa no Google com Sucesso
        Dado que a página do Google seja apresentada
        Quando eu inserir um texto na caixa de busca
        E acionar o botão Pesquisar
        Entao devo visualizar os resultados da busca
