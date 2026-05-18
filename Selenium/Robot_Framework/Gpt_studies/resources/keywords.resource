*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Launch Browser
    [Arguments]    ${url}    ${browser}

    Open Browser    ${url}    ${browser}
    Maximize Browser Window

Search In Google
    [Arguments]    ${search_txt}

    Input Text    name=q    ${search_txt}
    Press Keys    name=q    Enter
    Sleep    4s

Verify Search Result Title
    [Arguments]    ${expected_text}

    Title Should Be    ${expected_text}


Close Application
    Close Browser

