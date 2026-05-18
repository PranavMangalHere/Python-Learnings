*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Registration Test
    ${speed}    Get Selenium Speed
    Log To Console    ${speed}
    Open Browser    https://demowebshop.tricentis.com/register    chrome
    Maximize Browser Window

#    Set Selenium Speed    3 seconds

    Select Radio Button    Gender    M
    Input Text    xpath://input[@id = 'FirstName']    Pranav
    Input Text    xpath://input[@id = 'LastName']    Mangal
    Input Text    xpath://input[@id = 'Email']    pranavmangal9@gmail.com
