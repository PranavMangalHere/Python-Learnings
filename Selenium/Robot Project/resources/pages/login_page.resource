*** Settings ***
Library    SeleniumLibrary

Resource    ../locators/login_locators.resource

*** Keywords ***
Enter Username
    [Arguments]    ${username}
    Wait Until Element Is Visible    ${USERNAME_INPUT}
    Input Text    ${USERNAME_INPUT}    ${username}

Enter Password
    [Arguments]    ${password}
    Wait Until Element Is Visible    ${PASSWORD_INPUT}
    Input Password    ${PASSWORD_INPUT}    ${password}

Click Login Button
    Wait Until Element Is Visible    ${LOGIN_BUTTON}
    Click Button    ${LOGIN_BUTTON}

Login With Credentials
    [Arguments]    ${username}    ${password}
    Enter Username    ${username}
    Enter Password    ${password}
    Click Login Button

Verify Successful Login
    Wait Until Element Is Visible    ${PRODUCTS_TITLE}    timeout=10s
    Element Should Be Visible        ${PRODUCTS_TITLE}

Verify Login Error Message
    Wait Until Element Is Visible    ${ERROR_MESSAGE}    timeout=10s
    Element Should Be Visible        ${ERROR_MESSAGE}

Open Menu
    Wait Until Element Is Visible    ${MENU_BUTTON}    timeout=10s
    Click Button    ${MENU_BUTTON}

Click Logout
    Wait Until Element Is Visible    ${LOGOUT_LINK}    timeout=10s
    Click Element    ${LOGOUT_LINK}

Verify Logout Successful
    Wait Until Element Is Visible    ${LOGIN_BUTTON}    timeout=10s
    Element Should Be Visible        ${LOGIN_BUTTON}

Verify Locked User Error Message
    Wait Until Element Is Visible    ${ERROR_MESSAGE}    timeout=10s
    Element Text Should Be
    ...    ${ERROR_MESSAGE}
    ...    Epic sadface: Sorry, this user has been locked out.

