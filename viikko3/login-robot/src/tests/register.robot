
*** Settings *** 
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  pekka  pekka123
    Input Credentials  pekka  kalle123
    Output Should Contain  User with username pekka already exists

Register With Too Short Username And Valid Password
    Input Credentials  pe  pekka123
    Output Should Contain  Username too short


Register With Enough Long But Invald Username And Valid Password
    Input Credentials  AAA#¤  pekka123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  pekka  pekka
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Input Register Command
    Create User  pekka  pekka123
    