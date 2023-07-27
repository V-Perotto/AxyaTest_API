*** Settings ***
Library    ../../tests/Contato.py

*** Keywords  ***
Dado que envio dados para atualizar um contato
    [Arguments]    ${ID}    &{kwargs}
    Set Test Variable   ${ID}    
    ${contato}=    Create Dictionary    &{kwargs}
    Set Test Variable   ${contato}

Quando atualizar o contato
    ${response}    Contato.update_contato   ${ID}   ${contato}
    Set Test Variable   ${response}

Então os dados devem ser atualizados
    Should Be Equal     Contato atualizado com sucesso     ${response['message']}   
