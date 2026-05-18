*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}    https://www.practiceselenium.com/practice-form.html

*** Test Cases ***
TestingInputBox
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store. Home page title
    Click Link    //a[@class = 'ico-login']
    Sleep    4s
    ${email_txt}    Set Variable   id:Email
    
    Element Should Be Visible    ${email_txt}
    Element Should Be Enabled    ${email_txt}

    Input Text    ${email_txt}    pranavmangal9@gmail.com
    Sleep    3s
    Clear Element Text    ${email_txt}
    Sleep    3s
    Close Browser

*** Keywords ***

