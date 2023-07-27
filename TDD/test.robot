*** Settings ***
Library     BuiltIn
Library     OperatingSystem
Resource     keywords/create.robot
Resource     keywords/read.robot
Resource     keywords/update.robot
Resource     keywords/delete.robot
Resource     keywords/search.robot

*** Test Cases ***
Adiciono um contato válido
    Dado que envio os dados para criar um contato    Carlos   Alberto   carlosalberto@google.com    (41) 99999-9999
    Quando criar o contato
    Então devo receber o ID do contato

Leio um contato válido
    Dado que solicito a leitura de um contato       ${20}
    Quando envio o ID do contato
    Então devo receber os dados detalhados do contato

Atualizo um contato válido
    Dado que envio dados para atualizar um contato    ${21}    Nome=Zeca    Email=zeca@pagod.inho    Telefone=(21) 9999-9999
    Quando atualizar o contato
    Então os dados devem ser atualizados

Deleto um contato inválido
    Dado que solicito a exclusão de um contato      ${112}
    Quando excluir o contato
    Então o contato deve ser apagado

Procuro contatos com nomes semelhantes
    Dado que solicito a pesquisa pelo nome      Mar
    Quando eu pesquisar os contatos
    Então o resultado deve retornar nomes semelhantes 