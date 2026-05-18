*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    chrome
${url}    https://www.practiceselenium.com/practice-form.html

*** Test Cases ***
TestingInputBox
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

    Select From List By Label    continents    Australia
    Sleep    3s
    Select From List By Index    continents    6

    #list box
#    Unselect From List By Index
    