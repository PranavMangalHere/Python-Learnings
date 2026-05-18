*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Registration Test
    ${speed}    Get Selenium Speed
    Log To Console    ${speed}
    Open Browser    https://demowebshop.tricentis.com/register    chrome

#    Set Selenium Speed    3 seconds

    Open Browser    https://demo.nopcommerce.com/    chrome

    Sleep    2s

#    Close Browser
    Close All Browsers