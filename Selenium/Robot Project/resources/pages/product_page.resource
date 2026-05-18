*** Settings ***
Library    SeleniumLibrary
Library    Collections
Resource    ../locators/product_locators.resource

*** Keywords ***

Verify Product page is Loaded
    Wait Until Element Is Visible    ${PRODUCT_TITLE}
    Element Should Be Visible    ${PRODUCT_TITLE}

Verify All Products Are Visible
    ${products}=    Get Webelements    ${PRODUCT_ITEMS}
    Length Should Be    ${products}    6

Verify Product Prices are Visible
    ${prices}=    Get Webelements    ${PRODUCT_PRICES}

    FOR    ${price}    IN    @{prices}
        Element Should Be Enabled    ${price}
    END

Select Product Sort Option
    [Arguments]    ${option}
    Select From List By Label    ${SORT_DROPDOWN}    ${option}

Verify Products Sorted A To Z
    ${actual_list}=    Get WebElements    ${PRODUCT_NAMES}

    ${product_names}=    Create List

    FOR    ${item}    IN    @{actual_list}
        ${text}=    Get Text    ${item}
        Append To List   ${product_names}    ${text}
    END

    ${sorted_list}=    Copy List    ${product_names}
    Sort List    ${sorted_list}

    Lists Should Be Equal    ${product_names}    ${sorted_list}