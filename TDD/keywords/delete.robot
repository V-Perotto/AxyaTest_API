*** Settings ***
Library    ../../tests/Contato.py

*** Keywords  ***
Dado que solicito a exclusão de um contato
    [Arguments]     ${ID}
    Set Test Variable   ${ID}

Quando excluir o contato
    ${response}     Contato.delete_contato      ${ID}
    Set Test Variable   ${response}

Então o contato deve ser apagado
    Should Be Equal     Contato deletado com sucesso    ${response['message']}