*** Settings ***
Library    SeleniumLibrary
Resource    ../variables/global_variables.resource

*** Keywords ***
Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}    options=add_argument("--incognito")
    Maximize Browser Window
    Set Selenium Implicit Wait    7s
    Register Keyword To Run On Failure    Capture Page Screenshot

Close Application
    Close Browser

Capture Screenshot
    ${timestamp}=    Get Time    epoch
    Capture Page Screenshot
    ...    reports/screenshots/screenshot_${timestamp}.png