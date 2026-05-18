*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}    https://demo.nopcommerce.com/

*** Test Cases ***
Testing Radio Buttons and Check Boxes
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Speed    2seconds

    Select Radio Button    sex    mail

    Select Checkbox    BlackTea
    Unselect Checkbox    Blacktea