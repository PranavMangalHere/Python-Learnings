*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
LoginTest
    Open Browser    https://demo.nopcommerce.com/    chrome
    Click Link    xpath://a[text()= "Log in"]
    Sleep    14s
    Input Text    xpath://input[@class = 'email']    pranavmangal9@gmail.com
    Input Password    xpath://input[@id = 'Password']    1234qwer
    Click Element    xpath://button[contains(@class, "login-button")]