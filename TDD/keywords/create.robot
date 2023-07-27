*** Settings ***
Library    ../../tests/Contato.py
Library     Collections

*** Keywords  ***
Dado que envio os dados para criar um contato    
    [Arguments]    ${nome}    ${sobrenome}    ${endereco}    ${telefone}
    Set Test Variable    ${nome}     
    Set Test Variable    ${sobrenome}
    Set Test Variable    ${endereco}
    Set Test Variable    ${telefone}

Quando criar o contato
    ${contato}=    Create Dictionary    Nome=${nome}    Sobrenome=${sobrenome}    Email=${endereco}    Telefone=${telefone}
    Set Test Variable   ${contato}

    ${response}    Contato.create_contato    ${contato}
    Set Test Variable    ${response}

Então devo receber o ID do contato
    ${type_response}    Evaluate     type(${response['ID']})
    ${type_int}         Evaluate     type(${1})
    Should Be Equal     ${type_response}    ${type_int}