*** Settings ***
Documentation    Get requests tests
Library    RequestsLibrary
Library    String
Library    OperatingSystem
Library    ../venv/lib/site-packages/robot/libraries/Collections.py
Variables  ConfigurationVariables.py


*** Keywords ***



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
    Log    ${resp.json()}
    ${content}=  Set Variable     ${resp.json()}
    #${content}=  Set Variable    ${resp.content}
    ${size}=  Get Length   ${content}
    Log  ${size}
    Should Be Equal As Integers    ${size}    10
    Log    ${content}
    #${no_entries}=    Count Values In List    ${content}    uuid
    #Should Be Equal As Integers    ${no_entries}    10