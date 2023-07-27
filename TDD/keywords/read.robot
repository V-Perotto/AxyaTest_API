*** Settings ***
Library    ../../tests/Contato.py

*** Keywords  ***
Dado que solicito a leitura de um contato
    [Arguments]    ${ID}
    Set Test Variable    ${ID}

Quando envio o ID do contato
    ${response}    Contato.read_contato    ${ID}
    Set Test Variable    ${response}

Então devo receber os dados detalhados do contato
    Should Be Equal     ${ID}   ${response['id']}