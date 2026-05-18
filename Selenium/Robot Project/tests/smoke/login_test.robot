*** Settings ***
Resource    ../../resources/keywords/browser_keywords.resource
Resource    ../../resources/pages/login_page.resource
Resource    ../../resources/variables/global_variables.resource

Test Setup    Open Application
Test Teardown    Close Application

*** Test Cases ***
Verify Valid Login
    Login With Credentials    ${STANDARD_USER}    ${STANDARD_PASSWORD}
    Verify Successful Login

Verify Invalid Login
    Login With Credentials    ${INVALID_USER}    ${INVALID_PASSWORD}
    Verify Login Error Message

Verify Locked User Login
    Login With Credentials    ${LOCKED_USER}    ${LOCKED_PASSWORD}
    Verify Locked User Error Message

Verify Logout Functionality
    Login With Credentials    ${STANDARD_USER}    ${STANDARD_PASSWORD}
    Verify Successful Login
    Open Menu
    Click Logout
    Verify Logout Successful
