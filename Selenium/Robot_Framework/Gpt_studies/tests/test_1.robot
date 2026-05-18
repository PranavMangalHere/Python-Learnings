*** Settings ***
Library      SeleniumLibrary
Resource     ../resources/keywords.resource
Variables    ../variables/test_data.py

*** Test Cases ***
Google Search Test
    [Documentation]    This test verifies Google search functionality using Robot Framework
    [Tags]    smoke    regression    google

    Launch Browser    ${URL}    ${BROWSER}

    Search In Google    ${SEARCH_TEXT}

    Verify Search Result Title    ${EXPECTED_TITLE}

    Close Application