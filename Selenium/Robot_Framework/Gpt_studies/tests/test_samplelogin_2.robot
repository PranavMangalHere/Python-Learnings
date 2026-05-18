*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/

*** Test Cases ***
Login test
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    name=username
    Input Text    name:username    Admin
    Input Text    name:password    admin123

    Click Element    xpath://button[@type='submit']
    Wait Until Page Contains    Dashboard

    Capture Page Screenshot

    Close All Browsers

