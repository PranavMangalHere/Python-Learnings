*** Settings ***
Resource    ../../resources/keywords/browser_keywords.resource
Resource    ../../resources/pages/login_page.resource
Resource    ../../resources/pages/product_page.resource
Resource    ../../resources/variables/global_variables.resource

Test Setup    Open Application
Test Teardown        Close Application

*** Test Cases ***

Verify Products Are Displayed
    Login With Credentials    ${STANDARD_USER}    ${STANDARD_PASSWORD}

    Verify Product Page Is Loaded
    Verify All Products Are Visible

Verify Product Prices
    Login With Credentials    ${STANDARD_USER}    ${STANDARD_PASSWORD}

    Verify Product Page is Loaded
    Verify Product Prices Are Visible

Verify Product Sorting A-Z
    Login With Credentials    ${STANDARD_USER}    ${STANDARD_PASSWORD}

    Verify Product Page is Loaded

    Select Product Sort Option    Name (A to Z)

    Verify Products Sorted A To Z


