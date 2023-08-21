*** Settings ***
Documentation    Get requests tests
Library    RequestsLibrary
Library    String
Library    OperatingSystem
Library    Collections
Variables  ConfigurationVariables.py

*** Variables ***
${resp}            


*** Test Cases ***
Get_status_code
    ${resp}=    GET     ${base_url}
    Status Should Be    200    ${resp}


Get_content_type_should_be_text_html
    ${resp}=    GET      ${base_url}
    ${content_type}=  Get From Dictionary    ${resp.headers}    content-type
    Should Be Equal As Strings  text/html; charset=utf-8  ${content_type}

Get_order_should_be_10
    ${resp}=    GET    ${get_order_url}
    ${content}=  Set Variable     ${resp.json()}
    ${size}=  Get Length   ${content}
    Should Be Equal As Integers    ${size}    10
