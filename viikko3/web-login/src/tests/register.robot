*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Succeed 

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Invalid Password
    Set Username  pekka
    Set Password  pekkapekka
    Set Password Confirmation  pekkapekka
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Nonmatching password

Login After Successful Registration
    Set Username  jaakko
    Set Password  jaakko123
    Set Password Confirmation  jaakko123
    Submit Credentials
    Go To Main Page And Log Out
    Set Username  jaakko
    Set Password  jaakko123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  mikko
    Set Password  mikkomikko
    Set Password Confirmation  mikkomikko
    Submit Credentials
    Click Link Login
    Set Username  mikko
    Set Password  mikkomikko
    Submit Login
    Login Should Fail With Message  Invalid username or password


    