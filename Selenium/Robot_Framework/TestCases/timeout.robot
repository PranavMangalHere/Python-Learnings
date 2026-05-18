*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Registration Test
    ${speed}    Get Selenium Speed
    Log To Console    ${speed}
    Open Browser    https://demowebshop.tricentis.com/register    chrome
    Maximize Browser Window

#    Set Selenium Speed    3 seconds
#    Set Selenium Timeout    10 seconds
    Wait Until Page Contains    Register    # if  not found then it will wait for 5seconds default to change it use above statement

    Select Radio Button    Gender    M
    Input Text    xpath://input[@id = 'FirstName']    Pranav
    Input Text    xpath://input[@id = 'LastName']    Mangal
    Input Text    xpath://input[@id = 'Email']    pranavmangal9@gmail.com
