*** Settings ***
Library    ../../tests/Contato.py

*** Keywords  ***
Dado que solicito a pesquisa pelo nome      
    [Arguments]    ${nome}
    Set Test Variable   ${nome}

Quando eu pesquisar os contatos
    ${list_of_response}    Contato.search_contato   ${nome}
    Set Test Variable    ${list_of_response}   

Então o resultado deve retornar nomes semelhantes   
    ${type_response}    Evaluate     type(${list_of_response})
    ${type_list}        Evaluate     type([])
    Should Be Equal     ${type_response}   ${type_list}