*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.5 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    # seuraava rivi on kommentoitu toistaiseksi pois
    # Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Main Page
    Go To  ${HOME_URL}

Go To Register Page 
    Go To  ${REGISTER_URL}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Page Should Be Open
    Title Should Be  Register

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Go To Main Page And Log Out
    Click Link  Continue to main page
    Click Button  Logout

Submit Login 
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Click Link Login
    Click Link  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
